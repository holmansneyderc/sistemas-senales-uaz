<template>
  <v-app>
    <v-navigation-drawer app>
      <v-list>
        <v-list-item>
          <v-list-item-content>
            <v-menu offset-y>
              <template v-slot:activator="{ on, attrs }">
                <v-list-item-title v-bind="attrs" v-on="on">
                  Opciones
                </v-list-item-title>
              </template>
              <v-list>
                <v-list-item>
                  <v-list-item-title>Convolución</v-list-item-title>
                </v-list-item>
                <v-list-item>
                  <v-list-item-title>Discreta</v-list-item-title>
                </v-list-item>
                <v-list-item>
                  <v-list-item-title>Continua</v-list-item-title>
                </v-list-item>
              </v-list>
            </v-menu>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Menú</v-toolbar-title>
    </v-app-bar>
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  name: 'Menu',
  data() {
    return {
      drawer: false,
    };
  },
}
</script>
