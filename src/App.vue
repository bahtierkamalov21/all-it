<template lang="pug">
v-app
  main-navigation
  router-view
  the-bottom-navigation
  footer
    the-faq
  button-up
</template>

<script>
import MainNavigation from "@/components/MainNavigation";
import TheBottomNavigation from "@/components/TheBottomNavigation";
import TheFaq from "@/components/TheFaq";
import ButtonUp from "./components/ButtonUp";

export default {
  name: "App",
  components: {
    MainNavigation,
    TheBottomNavigation,
    TheFaq,
    ButtonUp,
  },
  data: () => ({}),
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
  --grey: #adb9c7;
}

h1 {
  font-size: 62px;
  line-height: 70px;
}

h2 {
  font-size: 42px;
  line-height: 42px;
}

.v-timeline-item__body {
  & > *:first-child {
    box-shadow: (--shadow-2xl) !important;

    & > * {
      font-weight: 700 !important;
    }
  }
}

.v-dialog__content.v-dialog__content--active {
  position: fixed;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10 !important;
  width: 100vw;
  height: 100vh;
  background-color: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(16px);

  & > *:first-child {
    overflow: initial;
    box-shadow: none !important;
  }
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

  &-item__content {
    padding: 12px;
  }
}

.input > div > div:first-child {
  box-shadow: none !important;
  padding: 12px 16px !important;
  font-weight: 500;
  font-size: 18px;
  letter-spacing: 0.04em;
  color: #232323 !important;
  background: linear-gradient(
    120.61deg,
    rgba(255, 188, 167, 0.1) 0%,
    rgba(255, 220, 209, 0.1) 100%
  ) !important;
  border-radius: 8px;
}

.v-menu__content.theme--dark.v-menu__content--fixed.menuable__content__active {
  border-radius: 10px;
  background: #232323;
  box-shadow: var(--shadow-lg) !important;
  font-weight: bold;
  transform: translateY(10px);
}

.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active {
  border-radius: 10px;
  background: white;
  box-shadow: var(--shadow-lg) !important;
  font-weight: bold;
  transform: translateY(10px);
}

.v-menu__content.theme--dark.v-menu__content--fixed.menuable__content__active.v-autocomplete__content {
  border-radius: 10px;
  background: #232323;
  box-shadow: var(--shadow-lg) !important;
  font-weight: bold;
  transform: translateY(10px);
}

.v-menu__content.theme--light.v-menu__content--fixed.menuable__content__active.v-autocomplete__content {
  border-radius: 10px;
  background: white;
  box-shadow: var(--shadow-lg) !important;
  font-weight: bold;
  transform: translateY(10px);
}

.theme--light.v-timeline::before {
  background: rgba(255, 255, 255, 0.15) !important;
}

.container {
  max-width: 1160px;
}

@keyframes hover-list-link {
  from {
    opacity: 0.2;
  }

  to {
    opacity: 1;
  }
}

@media screen and (max-width: 1086px) {
  h1 {
    font-size: 52px;
  }
}

@media screen and (max-width: 600px) {
  h1 {
    font-size: 32px;
  }

  h2 {
    font-size: 24px;
    line-height: 32px;
  }
}
</style>
