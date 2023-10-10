<template>
  <v-card class="fill-height">
    <v-layout fill-height>
      <v-navigation-drawer
        permanent
        location="right"
      >
        <v-list density="compact" nav>
          <v-list-item>
            <v-select
              :items="options"
              label="Tipo de señal"
              outlined
              v-model="selectedOption"
            ></v-select>
          </v-list-item>
          <v-list-item-group v-if="selectedOption === 'Señal continua'">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Titulo Señal Continua</v-list-item-title>
                <v-select
                  :items="optionsContinue"
                  label="Parametros de entrada"
                  outlined
                  v-model="selectedOptionContinue"
                ></v-select>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
          <v-list-item-group v-else-if="selectedOption === 'Señal discreta'">
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>Titulo Señal Discreta</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <!-- ... cualquier otro contenido para Señal Discreta ... -->
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
      <v-main style="min-height: 250px; width: 100%">
        <!-- Componente para Señal Continua -->
        <ContinuousComponent
          v-if="selectedOption === 'Señal continua'"
          :selectedOptionContinue="selectedOptionContinue"
        />

        <!-- Componente para Señal Discreta -->
        <DiscreteComponent v-else />

      </v-main>
    </v-layout>
  </v-card>
</template>

<script lang="ts">
import { defineComponent, ref, Ref, onBeforeMount, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import ContinuousComponent from '@/components/ContinuousComponent.vue';
import DiscreteComponent from '@/components/DiscreteComponent.vue';

export default defineComponent({
  components: {
    ContinuousComponent,
    DiscreteComponent,
  },
  setup() {
    const options = ref(['Señal discreta', 'Señal continua']);
    const optionsContinue = ref(['Criterios de existencia', 'funciones']);

    const selectedOption: Ref<string | null> = ref(null);
const selectedOptionContinue: Ref<string | null> = ref(null);

    const router = useRouter();
    const route = useRoute();

    onBeforeMount(() => {
      // Configura las opciones seleccionadas basadas en la ruta actual.
      switch (route.name) {
        case 'convolucion discreta':
          selectedOption.value = 'Señal discreta';
          break;
        case 'convolucion continua por funciones':
          selectedOption.value = 'Señal continua';
          selectedOptionContinue.value = 'funciones';
          break;
        case 'convolucion continua por criterios de existencia':
          selectedOption.value = 'Señal continua';
          selectedOptionContinue.value = 'Criterios de existencia';
          break;
      }
    });

    // Observa cambios en `selectedOption` y redirige según sea necesario.
    watch(selectedOption, (newVal) => {
      if (newVal === 'Señal discreta') {
        router.push({ name: 'convolucion discreta' });
      } else if (newVal === 'Señal continua' && selectedOptionContinue.value) {
        // En caso de que `selectedOptionContinue` ya tenga un valor, también navega.
        navigateToContinuousOption(selectedOptionContinue.value);
      }
    });

    // Observa cambios en `selectedOptionContinue` y redirige si `selectedOption` es 'Señal continua'.
    watch(selectedOptionContinue, (newVal) => {
      if (selectedOption.value === 'Señal continua') {
        navigateToContinuousOption(newVal);
      }
    });

    // Función para navegar basada en `selectedOptionContinue`.
    const navigateToContinuousOption = (option: string | null) => {
      if (option === 'funciones') {
        router.push({ name: 'convolucion continua por funciones' });
      } else if (option === 'Criterios de existencia') {
        router.push({ name: 'convolucion continua por criterios de existencia' });
      }
    };

    return { options, selectedOption, optionsContinue, selectedOptionContinue };
  },
});
</script>
