<template>
  <v-chart :option="chartOptions" autoresize style="height: 240px; width: 100%" />
</template>

<script setup lang="ts">
import { computed } from 'vue'
import VChart from 'vue-echarts'
import type { EChartsOption } from 'echarts'
import type { CallbackDataParams } from 'echarts/types/dist/shared'

// Tipagem dos pontos
const props = defineProps<{
  points: {
    x: number
    y: number
    label: string
    isCorrect: boolean
    type: 'guess' | 'hint'
    distance: number
  }[]
}>()

// Cores baseadas na distância
function getColorByDistance(distance: number): string {
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

// Opções do gráfico
const chartOptions = computed(() => {
  return {
    animation: false,
    grid: { left: 0, right: 0, top: 0, bottom: 0 },
    tooltip: {
      trigger: 'item',
      formatter: (param: CallbackDataParams) => {
        const data = param.data as { label: string }
        return data.label
      }
    },
    xAxis: {
      min: -1,
      max: 1,
      show: false,
      axisLine: { show: false },
      splitLine: { show: false }
    },
    yAxis: {
      min: -1,
      max: 1,
      show: false,
      axisLine: { show: false },
      splitLine: { show: false }
    },
    series: [
      {
        type: 'scatter',
        symbolSize: (_val: number[], params: { data: { isCorrect: boolean } }) =>
          params.data.isCorrect ? 16 : 10,
        data: props.points.map(p => ({
          value: [p.x, p.y],
          label: p.label,
          isCorrect: p.isCorrect,
          itemStyle: {
            color: p.isCorrect
              ? '#C8A700' // correto
              : p.type === 'hint'
              ? '#00BFAE' // dica
              : getColorByDistance(p.distance)
          }
        }))
      }
    ]
  } as EChartsOption
})
</script>
