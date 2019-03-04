<template>
     <v-toolbar app color="primary">
        <section id="logo">
          <v-toolbar-side-icon @click="cambio()" class="hidden-md-and-up"></v-toolbar-side-icon>
            <a href="#">
              <v-btn icon @click="home()" class="mx-3">
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
          <v-btn flat @click="home()">Inicio</v-btn>
          <v-btn flat @click="link('maestros')">Maestros</v-btn>
          <Dropdown nombre="Procesos" :items="procesos"  />
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>

import logo from "../../assets/Calca_TIC.png"
import Dropdown from "../menu/Dropdown"
export default {
    name:"Nav",
    data() {
      return {
        logo,
        procesos: [
        {name:"Reidencias",path:"recidencias"},
        {name:"Servicio", path: "servicio"}
      ]
      }
    },
    methods: {
      pruebaLink(path){
        console.log('path/', path)
      },
      link(name){
        this.$router.push({path:`/${name}`})
      },
      home(){
        this.$router.push({path:`/`})
      }
    },
    components:{
      Dropdown
    }

}
</script>