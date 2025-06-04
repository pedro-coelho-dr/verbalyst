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

          </q-toolbar>
        </div>
      </div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { Dark } from 'quasar'

const darkMode = ref(Dark.isActive)
const isDark = computed(() => Dark.isActive)

watch(darkMode, val => Dark.set(val))

const toggleDarkMode = () => {
  Dark.toggle()
  darkMode.value = Dark.isActive
}
</script>

