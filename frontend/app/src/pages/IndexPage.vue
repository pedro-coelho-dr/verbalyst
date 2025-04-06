<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md" style="max-width: 400px; width: 100%">
      <q-form @submit="submitGuess">
        <q-input
          filled
          v-model="guess"
          label="Digite sua palavra"
          lazy-rules
          :rules="[val => !!val || 'Campo obrigatório']"
        />
        <q-btn
          label="Enviar"
          type="submit"
          color="primary"
          class="q-mt-md full-width"
        />
      </q-form>

      <div v-if="error" class="text-negative q-mt-md">
        {{ error }}
      </div>

      <div class="q-mt-xl">
        <q-banner v-if="guesses.length === 0" class="bg-grey-2">
          Nenhuma tentativa ainda.
        </q-banner>
        <q-list v-else bordered>
          <q-item-label header>Tentativas</q-item-label>
          <q-item
            v-for="(item, index) in guesses"
            :key="index"
            :class="item.correct ? 'bg-green-1' : ''"
          >
            <q-item-section>{{ item.guess }}</q-item-section>
            <q-item-section side>{{ item.score }}</q-item-section>
          </q-item>
        </q-list>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { api } from 'boot/axios'
import axios from 'axios'


interface GuessResponse {
  guess: string
  score: number
  correct: boolean
}

const guess = ref<string>('')
const guesses = ref<GuessResponse[]>([])
const error = ref<string | null>(null)

const LOCALSTORAGE_KEY = 'verbalyst_guesses'

onMounted(() => {
  const saved = localStorage.getItem(LOCALSTORAGE_KEY)
  if (saved) {
    guesses.value = JSON.parse(saved) as GuessResponse[]
  }
})

watch(guesses, (newVal) => {
  localStorage.setItem(LOCALSTORAGE_KEY, JSON.stringify(newVal))
}, { deep: true })

const submitGuess = async () => {
  try {
    const res = await api.get<GuessResponse>('/guess', {
      params: { guess: guess.value }
    })

    error.value = null

    guesses.value.unshift({
      guess: res.data.guess,
      score: res.data.score,
      correct: res.data.correct
    })

    guess.value = ''
  } catch (err: unknown) {
    if (axios.isAxiosError(err) && err.response?.data?.detail) {
      error.value = err.response.data.detail
    } else {
      error.value = 'Erro ao consultar'
    }
  }
}
</script>
