<template lang="pug">
v-app
  main-navigation
  router-view
</template>

<script>
import MainNavigation from "./components/MainNavigation";

export default {
  name: "App",
  components: {
    MainNavigation,
  },
  data: () => ({}),
};
</script>

<style>
.v-application {
  font-family: "Poppins", "Roboto", sans-serif;
}
</style>
