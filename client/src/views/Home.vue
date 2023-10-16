<template>
  <div>
    <v-app>
      <v-main>
        <v-container>
          <v-row>
            <v-col cols="12" md="4" v-for="card in cards" :key="card.id">
              <router-link :to="card.route" class="no-underline">
                <v-card class="pa-3" elevation="3">
                  <v-card-title>
                    <v-icon left>{{card.icon}}</v-icon>{{ card.title }}
                  </v-card-title>
                  <v-card-text>
                    {{ card.content }}
                  </v-card-text>
                </v-card>
              </router-link>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
    </v-app>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      cards: [
        { id: 1, title: 'Convolución', content: 'Convolución' , icon: 'mdi-filter-variant', route: 'convolucion-discreta' },
        { id: 2, title: 'Series de Fourier', content: 'Series de Fourier' , icon: 'mdi-chart-line-variant', route: '' },
        { id: 3, title: 'Transformada de Fourier', content: 'Transformada de Fourier' , icon: 'mdi-chart-bell-curve', route: '' },
      ],
    };
  },
};
</script>


<style scoped>
/* Estilo para quitar el subrayado de los enlaces */
.no-underline {
  text-decoration: none;
}
</style>
