<template>
  <q-layout view="hHh Lpr lFf"> <!-- hHh: header scrolla com a página -->
    <q-header class="bg-primary text-white">
      <div class="row justify-center">
        <div style="max-width: 640px; width: 100%">
          <q-toolbar class="q-px-sm">
            <q-toolbar-title class="uncial-antiqua">
              VERBALYST
            </q-toolbar-title>

            <q-btn
              dense flat round
              :icon="isDark ? 'light_mode' : 'dark_mode'"
              @click="toggleDarkMode"
              class="q-mr-sm"
            />

            <q-btn
              dense flat round
              icon="account_circle"
              class="q-mr-sm"
            />

            <q-btn
              dense flat round
              icon="menu"
              @click="toggleRightDrawer"
            />
          </q-toolbar>
        </div>
      </div>
    </q-header>

    <q-drawer v-model="rightDrawerOpen" side="right" overlay bordered>
      <q-list>
        <q-item>
          <q-item-section>
            <q-toggle
              v-model="darkMode"
              label="Modo escuro"
              left-label
              color="secondary"
            />
          </q-item-section>
        </q-item>

        <q-separator class="q-my-sm" />

        <q-item-section class="q-pt-md">
          <div class="q-gutter-sm">
            <q-input
              v-model.number="tempGameId"
              label="ID do Jogo"
              type="number"
              dense
              outlined
              color="primary"
              :min="1"
              class="q-mb-sm"
              style="max-width: 120px"
            />
              <q-btn
              label="Confirmar"
              color="primary"
              dense
              unelevated
              class="q-mt-xs"
              style="width: 100px"
              @click="confirmGameId"
            />
          </div>
        </q-item-section>

      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { Dark, useQuasar } from 'quasar'
import { useGameId } from 'src/composables/useGameId'

const { gameId } = useGameId()
const $q = useQuasar()

const tempGameId = ref<number>(gameId.value)

const confirmGameId = () => {
  if (tempGameId.value < 1) {
    $q.notify({ type: 'negative', message: 'O ID deve ser maior ou igual a 1' })
    return
  }
  if (tempGameId.value === gameId.value) {
    $q.notify({ type: 'info', message: 'Esse jogo já está selecionado' })
    return
  }

  gameId.value = tempGameId.value
  $q.notify({ type: 'positive', message: `Jogo ${gameId.value} carregado` })
}

const rightDrawerOpen = ref(false)
const toggleRightDrawer = () => rightDrawerOpen.value = !rightDrawerOpen.value

const darkMode = ref(Dark.isActive)
const isDark = computed(() => Dark.isActive)

watch(darkMode, val => Dark.set(val))

const toggleDarkMode = () => {
  Dark.toggle()
  darkMode.value = Dark.isActive
}
</script>

