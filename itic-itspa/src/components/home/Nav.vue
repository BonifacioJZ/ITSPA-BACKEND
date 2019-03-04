<template>
     <v-toolbar app color="primary">
        <section id="logo">
          <v-toolbar-side-icon @click="cambio()" class="hidden-md-and-up"></v-toolbar-side-icon>
            <a href="#">
              <v-btn icon  class="mx-3">
                <v-img :src="logo" height="32px" width="32px"></v-img>
              </v-btn>
            </a>
        </section>
        <section class="hidden-sm-and-down">
          <v-toolbar-title class="headline text-uppercase">
            <span>ITIC</span>
          </v-toolbar-title>
        </section>
       <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-btn flat>Home</v-btn>
          <v-btn flat>Maestros</v-btn>
          <v-menu :nudge-width="100" offset-y>
            <template v-slot:activator="{ on }">
              <v-btn  flat v-on="on">
                Procesos
                <v-icon dark>arrow_drop_down</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-tile
            v-for="item in items"
            :key="item"
            @click=""
          >
            <v-list-tile-title v-text="item"></v-list-tile-title>
          </v-list-tile>
            </v-list>
          </v-menu>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>

import logo from "../../assets/Calca_TIC.png"
export default {
    name:"Nav",
    data() {
      return {
        logo,
        items: [
        'All', 'Family', 'Friends', 'Coworkers'
      ]
      }
    },
}
</script>