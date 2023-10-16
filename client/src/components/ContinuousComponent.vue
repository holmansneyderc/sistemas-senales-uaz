<template>
  <v-container fluid>
    <v-row class="equal-height">
      <v-col cols="6" class="d-flex align-stretch">
        <v-card flat class="flex">
          <v-card-title>x[n]</v-card-title>
          <SignalContinue :formData="formDataRight" />
        </v-card>
      </v-col>
      <v-col cols="6" class="d-flex align-stretch">
        <v-card flat class="flex">
          <v-card-title>h[n]</v-card-title>
          <SignalContinue :formData="formDataLeft" />
        </v-card>
      </v-col>
    </v-row>
  </v-container>



  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title class="d-flex justify-space-between align-center">
            <div>Salida</div>
            <div>
              <v-btn class="ml-4" @click="calculate" color="primary">Calcular</v-btn>
              <v-btn class="ml-4" @click="animatecalculate" color="primary">Animar</v-btn>
            </div>
           
          </v-card-title>
          <ConvolutionContinue :data="convolutionData" :key="componentKey"/>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
  
  
<script setup>





import { ref } from 'vue';
import axios from 'axios';
import SignalContinue from './SignalContinue.vue';
import ConvolutionContinue from './ConvolutionContinue.vue';


// Datos de la convolución (esto debería ser un objeto con la estructura adecuada)
const convolutionData = ref({
  xValues: [/* valores de x */],
  convolutionData: [/* resultados de la convolución */],
});

// En tu aplicación, probablemente llamarás a un servicio o realizarás cálculos para obtener estos datos.
// Por ahora, solo un ejemplo de datos para mostrar.




let formDataRight = ref('x >= -1 && x <= 1 ? 1 : 0');
let formDataLeft = ref('x >= -2 && x <= 2 ? 1 : 0');

// Ref para almacenar el resultado de la convolución
let convolutionResult = ref([]);
let componentKey = ref(Date.now());
const updateImpulseData = (newData, data) => {
  data = newData;
};

// Método para llamar al servicio
const calculate = async () => {
  try {
    const response = await axios.post(`${import.meta.env.VITE_API_URL}/convolve-continue`, {
      impulseDataLeft: formDataRight.value,
      impulseDataRight: formDataLeft.value
    });
    convolutionResult.value = response.data;
    // Llena los datos de ejemplo (reemplaza esto con tus datos reales)
    convolutionData.value.xValues = response.data.x_values;
    convolutionData.value.convolutionData = response.data.convolution_result;

    console.log(convolutionData)

    componentKey.value = Date.now();  // Forzar la actualización del componente hijo

  } catch (error) {
    console.error('Hubo un error al llamar al servicio:', error);
  }
};


const animatecalculate = async () => {
  try {
    const response = await axios.post(`${import.meta.env.VITE_API_URL}/convolve-continue`, {
      impulseDataLeft: formDataRight.value,
      impulseDataRight: formDataLeft.value,
      time: 0
    });
    convolutionResult.value = response.data;
    // Llena los datos de ejemplo (reemplaza esto con tus datos reales)
    convolutionData.value.xValues = response.data.x_values;
    convolutionData.value.convolutionData = response.data.convolution_result;

    console.log(convolutionData)

    componentKey.value = Date.now();  // Forzar la actualización del componente hijo

  } catch (error) {
    console.error('Hubo un error al llamar al servicio:', error);
  }
};
</script>