import { boot } from 'quasar/wrappers'
import axios from 'axios'
import type { AxiosInstance } from 'axios' // <- isso corrige o aviso do ESLint

declare module 'vue' {
  interface ComponentCustomProperties {
    $axios: typeof axios
    $api: AxiosInstance
  }
}

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL
})

export default boot(({ app }) => {
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = api
})

export { axios, api }
