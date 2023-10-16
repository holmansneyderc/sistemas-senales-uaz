<template>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-text-field v-model="funcStr" label="Función" placeholder="Inserta tu función"></v-text-field>
        </v-col>
        <v-col cols="12">
          <v-btn @click="graphFunction" color="primary">Graficar</v-btn>
          <div :id="'graph_' + instanceId"></div>
        </v-col>
      </v-row>
    </v-container>
</template>



<script>
import { ref, onMounted, getCurrentInstance } from 'vue';
import * as d3 from 'd3';

export default {
  props: {
    formData: String, // Propiedad para recibir los datos desde el componente padre
  },
  setup(props) {
    const funcStr = ref('x'); // Valor inicial: función x
    const instance = getCurrentInstance(); // Obtén la instancia actual
    const instanceId = instance.uid; // Crea un identificador único para esta instancia
    const textInput = ref(''); // Valor del campo de entrada de texto

    const graphFunction = () => {
      try {
        funcStr.value = props.formData; // Establece la función desde formData
        const func = new Function('x', `return ${funcStr.value}`);
        drawGraph(func, instanceId); // Pasa el identificador único
      } catch (e) {
        console.error('Error en la función ingresada: ', e);
      }
    };

    onMounted(() => {
      graphFunction(); // Dibuja un gráfico en el montaje con la función inicial
      textInput.value = ''; // Establece el valor inicial del campo de entrada de texto en blanco
    });

    return { funcStr, graphFunction, instanceId, textInput };
  },
};

function drawGraph(func, instanceId) {
  const margin = { top: 20, right: 20, bottom: 50, left: 50 },
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

  const x = d3.scaleLinear().domain([-10, 10]).range([0, width]);
  const y = d3.scaleLinear().domain([-10, 10]).range([height, 0]);

  const line = d3.line()
    .defined(d => !isNaN(d[1]))
    .x(d => x(d[0]))
    .y(d => y(d[1]));

  const data = Array.from({ length: width }, (_, i) => {
    const xi = x.invert(i);
    return [xi, func(xi)];
  });
  const graphId = `graph_${instanceId}`;

  d3.select(`#${graphId}`)
    .selectAll("*")
    .remove();

  const svg = d3.select(`#${graphId}`)
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // Agregar eje X
  const xAxis = d3.axisBottom(x).ticks(10);
  svg.append("g")
    .attr("class", "x-axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

  // Agregar etiqueta de eje X
  svg.append("text")
    .attr("class", "x-label")
    .attr("x", width / 2)
    .attr("y", height + margin.bottom)
    .style("text-anchor", "middle")
    .text("Eje X");

  // Agregar líneas de referencia en el eje X
  svg.selectAll(".x-line")
    .data(xAxis.scale().ticks(10))
    .enter()
    .append("line")
    .attr("class", "x-line")
    .attr("x1", d => x(d))
    .attr("x2", d => x(d))
    .attr("y1", 0)
    .attr("y2", height)
    .style("stroke", "#ccc");

  // Agregar eje Y
  const yAxis = d3.axisLeft(y).ticks(10);
  svg.append("g")
    .attr("class", "y-axis")
    .call(yAxis);

  // Agregar etiqueta de eje Y
  svg.append("text")
    .attr("class", "y-label")
    .attr("x", -margin.left)
    .attr("y", -margin.top)
    .style("text-anchor", "start")
    .text("Eje Y");

  // Agregar líneas de referencia en el eje Y
  svg.selectAll(".y-line")
    .data(yAxis.scale().ticks(10))
    .enter()
    .append("line")
    .attr("class", "y-line")
    .attr("x1", 0)
    .attr("x2", width)
    .attr("y1", d => y(d))
    .attr("y2", d => y(d))
    .style("stroke", "#ccc");

  svg.append("path")
    .data([data])
    .attr("fill", "none")
    .attr("stroke", "steelblue")
    .attr("stroke-linejoin", "round")
    .attr("stroke-linecap", "round")
    .attr("stroke-width", 1.5)
    .attr("d", line);
}
</script>

<style scoped>
/* Estilos de Vite.js en el archivo styles.css */
</style>
