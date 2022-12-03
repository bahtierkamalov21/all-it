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
  --index: (1vw + 1vh);
  --size-title: calc((1vw + 1vh) * 3.6);
}

html {
  scroll-behavior: smooth;
}

.v-application {
  background-color: var(--v-background-base) !important;
}
</style>
