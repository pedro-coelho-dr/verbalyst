import { ref, watch } from 'vue'

const gameId = ref<number>(parseInt(localStorage.getItem('verbalyst_game_id') || '1'))

watch(gameId, (val) => {
  localStorage.setItem('verbalyst_game_id', val.toString())
})

export function useGameId() {
  return { gameId }
}
