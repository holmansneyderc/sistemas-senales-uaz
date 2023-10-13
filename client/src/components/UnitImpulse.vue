<template>
  <v-container style="width: 100%;">
    <v-row :class="edit ? 'pa-5' : 'pa-14'">
      <v-col cols="12" :md="edit ? '4' : '12'" v-if="edit">

        <div>
          <h2>Tabla</h2>
          <table class="custom-table">
            <thead>
              <tr>
                <th>n</th>
                <th>Amplitud</th>
                <th> 
                  <v-btn @click="addRow" color="primary"><v-icon small>mdi-plus</v-icon></v-btn>
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(value, index) in impulseData" :key="index" :class="index % 2 === 0 ? 'even-row' : 'odd-row'">
                <td>{{ index }}</td>
                <td>
                  <input v-model="impulseData[index]" type="number" @input="updateChart" class="custom-input" />
                </td>
                <td><v-btn small @click="removeRow(index)"> <v-icon small>mdi-delete</v-icon>
                  </v-btn></td>
              </tr>
            </tbody>
          </table>

        </div>
      </v-col>
      <v-col cols="12" :md="edit ? '8' : '12'">
        <div>
          <h2>Gráfico</h2>
          <div class="chart" ref="chart"></div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import * as d3 from 'd3';

const chart = ref(null);
const { impulseData, edit } = defineProps(['impulseData', 'edit']);

onMounted(() => {
  drawChart();
});

// Método para añadir una nueva fila
const addRow = () => {
  impulseData.push(0); // o el valor por defecto que desees
  updateChart(); // Refrescar el gráfico
};

// Método para eliminar una fila específica
const removeRow = (index) => {
  impulseData.splice(index, 1); // Eliminar el ítem
  updateChart(); // Refrescar el gráfico
};

onUnmounted(() => {
  d3.select(chart.value).selectAll('*').remove();
});
const emit = defineEmits(['updateData']);
const drawChart = () => {
  if (!chart.value) return;

  const margin = { top: 10, right: 30, bottom: 30, left: 40 };
  const width = edit ? 400 - margin.left - margin.right : chart.value.clientWidth - margin.left - margin.right;
  const height = 200 - margin.top - margin.bottom;

  d3.select(chart.value).selectAll('*').remove();

  const yDomain = d3.extent(impulseData);
  const y = d3.scaleLinear().domain(yDomain).nice().range([height, 0]);

  const svg = d3
    .select(chart.value)
    .append('svg')
    .attr('width', width + margin.left + margin.right)
    .attr('height', height + margin.top + margin.bottom)
    .append('g')
    .attr('transform', `translate(${margin.left},${margin.top})`);

  const x = d3.scaleLinear().domain([0, impulseData.length - 1]).range([0, width]);

  svg
    .selectAll('line')
    .data(impulseData)
    .enter()
    .append('line')
    .attr('x1', (d, i) => x(i))
    .attr('y1', (d) => y(d))
    .attr('x2', (d, i) => x(i))
    .attr('y2', y(0))
    .attr('stroke', 'blue')
    .attr('stroke-width', 2);

  svg
    .append('line')
    .attr('x1', 0)
    .attr('y1', y(0))
    .attr('x2', width)
    .attr('y2', y(0))
    .attr('stroke', 'black')
    .attr('stroke-width', 1);

  svg
    .append('line')
    .attr('x1', 0)
    .attr('y1', 0)
    .attr('x2', 0)
    .attr('y2', height)
    .attr('stroke', 'black')
    .attr('stroke-width', 1);

  svg
    .selectAll('.x-label')
    .data(impulseData)
    .enter()
    .append('text')
    .attr('class', 'x-label')
    .attr('x', (d, i) => x(i))
    .attr('y', y(0) + 15)
    .attr('text-anchor', 'middle')
    .text((d, i) => `n=${i}`);

  svg
    .selectAll('.y-label')
    .data(impulseData)
    .enter()
    .append('text')
    .attr('class', 'y-label')
    .attr('x', (d, i) => x(i))
    .attr('y', (d) => y(d) - 10)
    .attr('text-anchor', 'middle')
    .attr('opacity', 0.2) // Agrega esta línea para la transparencia
    .text((d) => d.toFixed(2));
  svg
    .append('text')
    .attr('x', -15)
    .attr('y', -10)
    .attr('text-anchor', 'end')
    .text('Amplitud');

  // Agregando el eje Y
  const yAxis = d3.axisLeft(y);
  svg.append("g")
    .attr("class", "y-axis")
    .call(yAxis);

};


const updateChart = () => {
  emit('updateData', impulseData);
  drawChart();
};

watch(
  () => edit,
  () => {
    drawChart();
  },
  { immediate: true }
);
</script>

<style scoped>
.custom-table {
  width: 100%;
  border-collapse: collapse;
}

.custom-table th,
.custom-table td {
  padding: 1px 5px;
  border: 1px solid #ccc;
  text-align: center;
  width: auto;
}

.even-row {
  background-color: #f2f2f2;
}

.odd-row {
  background-color: #ffffff;
}

.custom-input {
  max-width: 50px;
}
</style>
