<template lang="pug">
v-app
  main-navigation
  router-view
  the-bottom-navigation
  footer
    the-faq
</template>

<script>
import MainNavigation from "@/components/MainNavigation";
import TheBottomNavigation from "@/components/TheBottomNavigation";
import TheFaq from "@/components/TheFaq";

export default {
  name: "App",
  components: {
    MainNavigation,
    TheBottomNavigation,
    TheFaq,
  },
  data: () => ({}),
  created() {
    // Determine whether the user is authorized
    this.$store.commit("setUser", localStorage.getItem("user"));
    // Commit theme in store
    this.$store.commit("changeTheme", this.$vuetify.theme.dark);
  },
};
</script>

<style lang="scss">
:root {
  --base-shadow: 0 0 10px -8px var(--v-color_shadow-base);
  --index: (1vw + 1vh);
  --size-title: calc((1vw + 1vh) * 3.05);
  --section-title: calc(var(--index) * 2);
  --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1),
    0 4px 6px -4px rgb(0 0 0 / 0.1);
  --custom-blue: #1867c0;
}

html {
  scroll-behavior: smooth;
}

.v-application {
  background-color: var(--v-background-base) !important;
  font-family: "Montserrat", "Roboto", sans-serif;
}

.v-list {
  background-color: transparent !important;

  &-group {
    overflow: hidden;
  }
}

.theme--light.v-timeline::before {
  background: rgba(255, 255, 255, 0.15) !important;
}

.field-sign .v-input__control .v-text-field__details {
  margin-left: 24px !important;
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
