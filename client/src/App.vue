<template>
  <v-card>
    <v-layout>
      <!-- Barra superior con tu nombre, materia y logo de la universidad -->
      <v-app-bar app color="gray">
        <!-- Logo de la universidad (ajusta la URL de la imagen según sea necesario) -->
        <v-img src="@/assets/holman.png" max-height="40" class="mr-4"></v-img>

        <!-- Texto con tu nombre y el nombre de la materia con padding -->
        <div class="pr-4"> <!-- Agrega un padding a la izquierda (por ejemplo, 4 unidades) -->
          <div class="caption">Señales y sistemas</div>
        </div>
      </v-app-bar>

      <!-- Menú lateral plegable -->
      <v-navigation-drawer
        expand-on-hover
        rail
      >
        <v-list>
          <v-list-item
            prepend-avatar="@/assets/holman.png"
            title="Holman Cabezas"
            subtitle="holmanc@uaz.edu.mx"
          ></v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item prepend-icon="mdi-filter-variant" title="Convolución" value="myfiles"></v-list-item>
          <v-list-item prepend-icon="mdi-chart-line-variant" title="Series de Fourier" value="shared"></v-list-item>
          <v-list-item prepend-icon="mdi-chart-bell-curve" title="Transformada de Fourier" value="starred"></v-list-item>
        </v-list>
      </v-navigation-drawer>

      <!-- Contenido de la página -->
      <v-main style="height: 250px">
        <router-view />
      </v-main>
    </v-layout>
  </v-card>
</template>
