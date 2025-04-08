import { Dark, setCssVar } from 'quasar'
import { watch } from 'vue'

export default () => {
  const applyThemeColors = (isDark: boolean) => {
    if (isDark) {
      setCssVar('positive', '#21BA45')
      setCssVar('negative', '#FF5555')
      setCssVar('info', '#58C7F3')
      setCssVar('warning', '#FFC107')
    } else {
      setCssVar('positive', '#056E22')
      setCssVar('negative', '#B00020')
      setCssVar('info', '#026690')
      setCssVar('warning', '#AD7E00')
    }
  }

  // Aplica tema inicialmente
  applyThemeColors(Dark.isActive)

  // Observa mudanças no modo escuro
  watch(
    () => Dark.isActive,
    (newVal) => {
      applyThemeColors(newVal)
    }
  )
}
