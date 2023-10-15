<template>
  <v-card>
    <v-layout>
      <!-- Barra superior con tu nombre, materia y logo de la universidad -->
      <v-app-bar app color="gray">
        <v-row no-gutters>
          <!-- Columna de texto -->
          <v-col cols="8" class="pl-4 pr-4 d-flex align-center"> <!-- Añadido d-flex y align-center -->
            <div class="caption">Señales y sistemas</div>
          </v-col>

          <!-- Columna de logo -->
          <v-col cols="4" class="d-flex justify-end"> <!-- Ajustado a 4 y agregado text-end para alinear a la derecha -->
            <v-img  class="pl-4" src="@/assets/logo.png" max-height="40" max-width="80" width="auto"></v-img> <!-- Añadido width="auto" -->
          </v-col>
        </v-row>
      </v-app-bar>


      <!-- Menú lateral plegable -->
      <v-navigation-drawer expand-on-hover rail>
        <v-list>
          <v-list-item prepend-avatar="@/assets/holman.png" title="Holman Cabezas"
            subtitle="holmanc@uaz.edu.mx"></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-filter-variant" title="Convolución" value="myfiles"></v-list-item>
          <v-list-item prepend-icon="mdi-chart-line-variant" title="Series de Fourier" value="shared"></v-list-item>
          <v-list-item prepend-icon="mdi-chart-bell-curve" title="Transformada de Fourier" value="starred"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <!-- Contenido de la página -->
      <v-main class="flex-grow-1 width-100">
        <router-view />
      </v-main>
    </v-layout>
  </v-card>
</template>
