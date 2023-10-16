<template>
  <div>
    <v-card>
      <v-card-title>Gráfico de Convolución</v-card-title>
      <svg ref="svg"></svg>
    </v-card>
  </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import * as d3 from 'd3';

export default {
  props: {
    data: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const svg = ref(null);

    onMounted(() => {
      drawGraph(props.data);
    });

    watch(() => props.data, (newData) => {
      drawGraph(newData);
    });

    const drawGraph = (data) => {
      const container = svg.value.parentElement; // Obtén el contenedor padre del SVG
      const containerWidth = container.clientWidth;
      const containerHeight = container.clientHeight;

      const margin = { top: 20, right: 20, bottom: 30, left: 40 };
      const width = containerWidth - margin.left - margin.right;
      const height = containerHeight - margin.top - margin.bottom;

      const x = d3
        .scaleLinear()
        .domain(d3.extent(data.xValues))
        .nice()
        .range([margin.left, width - margin.right]);

      const y = d3
        .scaleLinear()
        .domain([0, d3.max(data.convolutionData)])
        .nice()
        .range([height - margin.bottom, margin.top]);

      const line = d3
        .line()
        .x((d) => x(d[0]))
        .y((d) => y(d[1]));

      const svgElement = d3.select(svg.value);

      svgElement.selectAll('*').remove();

      svgElement
        .attr('width', containerWidth) // Establece el ancho del SVG al ancho del contenedor
        .attr('height', containerHeight) // Establece el alto del SVG al alto del contenedor
        .append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);

      svgElement
        .append('path')
        .datum(data.xValues.map((xVal, i) => [xVal, data.convolutionData[i]]))
        .attr('fill', 'none')
        .attr('stroke', 'steelblue')
        .attr('stroke-linejoin', 'round')
        .attr('stroke-linecap', 'round')
        .attr('stroke-width', 1.5)
        .attr('d', line);

      svgElement
        .append('g')
        .attr('class', 'x-axis')
        .attr('transform', `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x));

      svgElement
        .append('g')
        .attr('class', 'y-axis')
        .attr('transform', `translate(${margin.left},0)`)
        .call(d3.axisLeft(y));
    };

    return {
      svg,
    };
  },
};
</script>

<style scoped>
/* Estilos personalizados según tus necesidades */
</style>
