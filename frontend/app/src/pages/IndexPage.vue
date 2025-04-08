<template>
  <q-page class="flex flex-top justify-center q-pt-xl">
    <div class="q-pa-md" style="max-width: 400px; width: 100%">

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

        <q-btn
          label="Desisto"
          color="grey-8"
          text-color="white"
          @click="giveUp"
          class="q-px-md"
          rounded
          unelevated
        />
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
              {{ item.guess }}
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
              {{ item.score.toFixed(2) }}
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


const { gameId } = useGameId()

interface GuessResponse {
  guess: string
  score: number
  correct: boolean
}

const guess = ref('')
const guesses = ref<GuessResponse[]>([])
const error = ref<string | null>(null)
const hintCount = ref<number>(3)

const LOCALSTORAGE_KEY = computed(() => `verbalyst_guesses_${gameId.value}`)
const HINT_COUNT_KEY = computed(() => `verbalyst_hints_${gameId.value}`)

onMounted(loadLocalData)
watch(gameId, loadLocalData)

function loadLocalData() {
  const savedGuesses = localStorage.getItem(LOCALSTORAGE_KEY.value)
  guesses.value = savedGuesses ? JSON.parse(savedGuesses) : []
  const savedHints = localStorage.getItem(HINT_COUNT_KEY.value)
  hintCount.value = savedHints ? parseInt(savedHints, 10) : 3
}

watch(guesses, val => {
  localStorage.setItem(LOCALSTORAGE_KEY.value, JSON.stringify(val))
}, { deep: true })

watch(hintCount, val => {
  localStorage.setItem(HINT_COUNT_KEY.value, val.toString())
})

const submitGuess = async () => {
  try {
    const res = await api.get<GuessResponse>(`guess/${gameId.value}/${guess.value}`)
    error.value = null
    guesses.value.unshift(res.data)
    guess.value = ''
  } catch (err: unknown) {
    if (axios.isAxiosError(err) && err.response?.data?.detail) {
      error.value = err.response.data.detail
    } else {
      error.value = 'Erro ao consultar'
    }
  }
}

const useHint = () => {
  if (hintCount.value > 0) {
    console.log('Usando dica...')
    hintCount.value--
  }
}

const giveUp = () => {
  console.log('Desistiu.')
}

const sortedGuesses = computed(() => {
  return [...guesses.value].sort((a, b) => {
    if (a.correct && !b.correct) return -1
    if (!a.correct && b.correct) return 1
    return b.score - a.score
  })
})

const getItemStyle = (item: GuessResponse): Record<string, string> => {
  if (item.correct) {
    return {
      backgroundColor: '#C8A700', // cor dourada
      color: '#1A1A1A'
    }
  }
  return {
    backgroundColor: getScoreColorHex(item.score),
    color: '#F5F5F5'
  }
}

const getScoreColorHex = (score: number): string => {
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
