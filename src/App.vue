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
  --section-title: calc(var(--index) * 2);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  --text-4xl: 2.25rem;
}

html {
  scroll-behavior: smooth;
}

.v-application {
  background-color: var(--v-background-base) !important;
}

.v-list {
  background-color: transparent !important;
}

@keyframes hover-list-link {
  from {
    opacity: 0.2;
  }

  to {
    opacity: 1;
  }
}
</style>
