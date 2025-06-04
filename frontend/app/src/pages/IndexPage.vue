<template>
  <q-page class="flex flex-top justify-center q-pt-xl">
    <div class="q-pa-md" style="max-width: 400px; width: 100%">
      <ScatterMap
        :points="guesses.map(g => ({
          x: g.x,
          y: g.y,
          label: g.guess,
          isCorrect: g.correct,
          type: 'guess',
          distance: g.distance
        }))"
      />

      <!-- Campo de entrada -->
      <q-form @submit="submitGuess">
        <q-input
          v-model="guess"
          placeholder="Digite uma palavra..."
          dense
          outlined
          square
          hide-bottom-space
          class="q-mb-md text-subtitle1 custom-input"
          :input-style="{ textAlign: 'center' }"
        />
      </q-form>

      <!-- Erro -->
      <div v-if="error" class="text-negative q-mt-md text-center">
        {{ error }}
      </div>

      <!-- Botões de ação -->
      <div class="row justify-end q-gutter-sm q-mt-md q-mb-lg">
        <q-btn
          label="Dica"
          color="grey-8"
          text-color="white"
          :disable="hintCount <= 0"
          @click="useHint"
          class="q-px-md"
          rounded
          unelevated
        >
          <q-badge color="grey-4" text-color="black" class="q-ml-sm">
            {{ hintCount }}
          </q-badge>
        </q-btn>


      </div>

      <!-- Lista de tentativas -->
      <q-list v-if="sortedGuesses.length > 0">
        <q-item
          v-for="(item, index) in sortedGuesses"
          :key="index"
          class="q-my-xs"
          style="padding: 0"
        >
          <div
            class="row items-center justify-between q-pa-sm rounded-borders full-width"
            :style="getItemStyle(item)"
          >
            <div
              class="text-subtitle1 q-px-sm q-py-xs"
              style="
                background-color: #f5f5f5;
                color: #1a1a1a;
                border-radius: 8px;
                max-width: 75%;
                overflow-wrap: break-word;
              "
            >
              {{ item.guess || '-' }}
            </div>

            <div
              class="text-subtitle2 q-px-sm q-py-xs text-dark"
              style="
                background-color: #f5f5f5;
                color: #1a1a1a;
                border-radius: 8px;
                min-width: 40px;
                text-align: center;
              "
            >
              {{ item.distance?.toFixed ? item.distance.toFixed(0) : '-' }}
            </div>
          </div>
        </q-item>
      </q-list>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, computed } from 'vue'
import { api } from 'boot/axios'
import axios from 'axios'
import { useGameId } from 'src/composables/useGameId'
import ScatterMap from 'components/ScatterMap.vue'

const { gameId } = useGameId()
const MAX_HINTS = 10

const guess = ref('')
const guesses = ref<GuessResponse[]>([])
const error = ref<string | null>(null)
const hintCount = ref<number>(MAX_HINTS)
const hintNumbersUsed = ref<number[]>([])

interface GuessResponse {
  guess: string
  distance: number
  x: number
  y: number
  correct: boolean
}

const LOCALSTORAGE_KEY = computed(() => `verbalyst_guesses_${gameId.value}`)
const HINT_COUNT_KEY = computed(() => `verbalyst_hints_${gameId.value}`)
const USED_HINT_NUMBERS_KEY = computed(() => `verbalyst_hint_numbers_${gameId.value}`)

onMounted(loadLocalData)
watch(gameId, loadLocalData)

function loadLocalData() {
  if (gameId.value === null) return

  guesses.value = JSON.parse(localStorage.getItem(LOCALSTORAGE_KEY.value) || '[]')
  hintCount.value = parseInt(localStorage.getItem(HINT_COUNT_KEY.value) || `${MAX_HINTS}`, 10)
  hintNumbersUsed.value = JSON.parse(localStorage.getItem(USED_HINT_NUMBERS_KEY.value) || '[]')
}


watch(guesses, val => {
  localStorage.setItem(LOCALSTORAGE_KEY.value, JSON.stringify(val))
}, { deep: true })

watch(hintCount, val => {
  localStorage.setItem(HINT_COUNT_KEY.value, val.toString())
})

watch(hintNumbersUsed, val => {
  localStorage.setItem(USED_HINT_NUMBERS_KEY.value, JSON.stringify(val))
}, { deep: true })

function normalizeInput(text: string): string {
  return text
    .normalize('NFD') // separa acentos
    .replace(/[\u0300-\u036f]/g, '') // remove acentos
    .trim()
    .toLowerCase()
}

const submitGuess = async () => {
  const input = guess.value
  const normalized = normalizeInput(input)
  const alreadyUsed = guesses.value.some(g => normalizeInput(g.guess) === normalized)

  if (!normalized || alreadyUsed) {
    error.value = alreadyUsed ? 'Palavra já usada.' : null
    guess.value = ''
    return
  }

  try {
    const res = await api.get<GuessResponse>(`/daily/guess/${input.trim()}`)
    error.value = null
    guesses.value.unshift({
      ...res.data,
      guess: res.data.guess // mantém original para exibir com acento
    })
    guess.value = ''
  } catch (err) {
    error.value = axios.isAxiosError(err) && err.response?.data?.detail
      ? err.response.data.detail
      : 'Erro ao consultar'
  }
}

const useHint = async () => {
  if (hintCount.value <= 0) return

  const hintNumber = MAX_HINTS - hintCount.value + 1
  try {
    const res = await api.get(`/daily/hint/${hintNumber}`)
    const original = res.data.word
    const normalized = normalizeInput(original)
    const alreadyUsed = guesses.value.some(g => normalizeInput(g.guess) === normalized)

    if (!alreadyUsed) {
      guesses.value.unshift({
        guess: original,
        distance: Math.round(res.data.distance),
        x: res.data.x,
        y: res.data.y,
        correct: false
      })
    }

    hintNumbersUsed.value.push(hintNumber)
    hintCount.value--
  } catch (err) {
    console.error('Erro ao buscar dica', err)
  }
}

const sortedGuesses = computed(() => {
  return [...guesses.value].sort((a, b) => {
    if (a.correct && !b.correct) return -1
    if (!a.correct && b.correct) return 1
    return a.distance - b.distance
  })
})

const getItemStyle = (item: GuessResponse): Record<string, string> => {
  if (item.correct) {
    return {
      backgroundColor: '#C8A700',
      color: '#1A1A1A'
    }
  }
  return {
    backgroundColor: getScoreColorHex(item.distance),
    color: '#F5F5F5'
  }
}

function getScoreColorHex(distance: number): string {
  const score = Math.max(0, 100 - distance / 100)
  if (score >= 90) return '#311B92'
  if (score >= 80) return '#4527A0'
  if (score >= 70) return '#512DA8'
  if (score >= 60) return '#5E35B1'
  if (score >= 50) return '#673AB7'
  if (score >= 40) return '#7E57C2'
  if (score >= 30) return '#9575CD'
  return '#B39DDB'
}
</script>
