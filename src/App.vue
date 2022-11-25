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
:root {
  --base-shadow: 0 0 10px -8px var(--v-color_shadow-base);
}

html {
  scroll-behavior: smooth;
}

.v-application {
  font-family: "Poppins", "Roboto", sans-serif;
  background-color: var(--v-background-base) !important;
}
</style>
