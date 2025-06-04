import { ref, watch } from 'vue'

const gameId = ref<number | null>(null)

async function fetchGameId() {
  try {
    const res = await fetch('/verb/daily/game')
    const data = await res.json()
    gameId.value = data.game_id
    localStorage.setItem('verbalyst_game_id', data.game_id.toString())
  } catch (e) {
    console.error('Failed to fetch daily game_id:', e)
    // fallback para localStorage
    const fallbackId = parseInt(localStorage.getItem('verbalyst_game_id') || '1')
    gameId.value = fallbackId
  }
}

void fetchGameId()


watch(gameId, (val) => {
  if (val !== null) {
    localStorage.setItem('verbalyst_game_id', val.toString())
  }
})

export function useGameId() {
  return { gameId }
}