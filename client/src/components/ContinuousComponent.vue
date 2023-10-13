<template>
  <v-container fluid>
    <v-row class="equal-height">
      <v-col cols="6" class="d-flex align-stretch">
        <v-card flat class="flex">
          <v-card-title>x[n]</v-card-title>
          <SignalContinue />
        </v-card>
      </v-col>
      <v-col cols="6" class="d-flex align-stretch">
        <v-card flat class="flex">
          <v-card-title>h[n]</v-card-title>
          <SignalContinue />
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
              <v-btn @click="calculate" color="primary">Calcular</v-btn>
            </v-card-title>
  
            <UnitImpulse :impulseData="convolutionResult" :key="componentKey" :edit="false" v-if="convolutionResult.length > 0" />
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  import SignalContinue from './SignalContinue.vue';
  
  let impulseDataLeft = ref([0,0,1, -1, 3, 2,0,0]);
  let impulseDataRight = ref([0,0,2, 1, 4, 3, 2,0,0]);
  
  // Ref para almacenar el resultado de la convolución
  let convolutionResult = ref([]);
  let componentKey = ref(Date.now());
  const updateImpulseData = (newData, data) => {
    data = newData;
  };
  
  // Método para llamar al servicio
  const calculate = async () => {
    try {
      const response = await axios.post('http://localhost:5000/convolve', {
        impulseDataLeft: impulseDataLeft.value,
        impulseDataRight: impulseDataRight.value
      });
      convolutionResult.value = response.data;
      componentKey.value = Date.now();  // Forzar la actualización del componente hijo
  
    } catch (error) {
      console.error('Hubo un error al llamar al servicio:', error);
    }
  };
  </script>