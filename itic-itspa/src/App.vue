<template>
  <v-app>
    <NavBar></NavBar>
    <v-content>
       <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import NavBar from "./views/NavBar"
import Home from "./views/Home"
export default {
  name: 'App',
  components: {
    NavBar,
    Home
  },
  data () {
    return {
      //
    }
  },
}
</script>
