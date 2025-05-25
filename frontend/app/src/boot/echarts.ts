import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { ScatterChart } from 'echarts/charts'
import {
  TooltipComponent,
  GridComponent
} from 'echarts/components'

use([
  CanvasRenderer,
  ScatterChart,
  TooltipComponent,
  GridComponent
])

