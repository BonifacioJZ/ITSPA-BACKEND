<template>
  <v-app>
    <NavBar></NavBar>
    <v-content>
   
    </v-content>
  </v-app>
</template>

<script>
import NavBar from "./views/NavBar"

export default {
  name: 'App',
  components: {
    NavBar
  },
  data () {
    return {
      //
    }
  },
}
</script>
