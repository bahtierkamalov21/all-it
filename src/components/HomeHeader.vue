<template lang="pug">
div
  div(class="header")
    div(class="header-wrapper")
      div
      div
        shapes-home-header
    v-container(class="header-container")
      v-col 
        v-row(class="align-center") 
          div(class="left")
            v-chip(color="primary pl-7") Frontend Backend | Web Developers
              span(class="status")
            h1(class="title mt-6 mb-10") {{ $t("header__h1") }}
            h2(class="subtitle pa-0") 
              | {{ $t("modern") }}
              br
              | {{ $t("projects") }}
              span WCAG 3.0
            v-btn(class="left-button mt-6" color="primary" width="320" min-width="62" min-height="62")
              span(class="text-capitalize") {{ $t("discuss") }}
                span(class="text-lowercase")  {{ $t("project") }}
            marquee(class="marquee" behavior="alternate", direction="right")
              ul
                li sacascasc 
                li cascacascas 
          div(class="right")
</template>

<script>
import ShapesHomeHeader from "./ShapesHomeHeader.vue";
import { mapState } from "vuex";

export default {
  name: "HomeHeader",
  components: { ShapesHomeHeader },
  data() {
    return {
      container: null,
      colorsStatus: ["red", "blue"],
      elementStatusCircle: null,
    };
  },
  computed: {
    ...mapState(["theme"]),
  },
  watch: {
    theme() {
      this.changeBackgroundContainer();
    },
  },
  methods: {
    changeBackgroundContainer() {
      if (this.theme) {
        this.container.style.backgroundColor = "#262626D9";
      } else {
        this.container.style.backgroundColor = "rgba(255, 255, 255, 0.6)";
      }
    },
    changeColorsStatus() {
      const index = Math.floor(Math.random() * this.colors.length);
      this.elementStatusCircle.setAttribute("fill", this.colors[index]);
    },
  },
  mounted() {
    this.container = document.querySelector(".header-container");
    this.elementStatusCircle = document.querySelector(".status");
  },
};
</script>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  height: calc(100vh - 80px);
  margin-top: 80px;
  overflow: hidden;

  &-wrapper {
    width: 100%;
    display: flex;
    align-items: center;

    & > *:first-child {
      width: 50%;
    }

    & > *:last-child {
      width: 50%;
      height: calc(100vh - 80px);
      position: relative;
    }
  }

  &-container {
    position: absolute;
    background-color: rgba(255, 255, 255, 0.6);
    backdrop-filter: blur(12px);
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 12px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.08);
    padding: 32px;
    min-height: calc(100% - 92px);
  }
}

.status {
  display: block;
  width: 10px;
  height: 10px;
  background-color: red;
  position: absolute;
  left: 12px;
  border-radius: 20px;
}

.marquee {
  position: absolute;
  bottom: 32px;
  left: 32px;
}

.left {
  width: 50%;

  &-button {
    font-size: 18px !important;
    font-weight: 600;
  }
}

.title {
  font-size: 5rem !important;
  font-weight: 800;
}

.subtitle {
  font-size: 4rem;
  font-weight: 600;
  line-height: 4rem;
  padding: 10px;
  padding-right: 20px;
  display: inline-block;

  & > span {
    font-size: 1.5rem;
    color: #fff;
    font-weight: 500;
    padding: 8px 16px;
    border-radius: 120px;
    bottom: 10px;
    left: 10px;
    position: relative;
    background-color: #1976d2;
  }
}

@media screen and (max-width: 900px) {
  .header {
    &-container {
      width: 92.2%;
    }
  }
}

@media screen and (max-width: 560px) {
  .header {
    &-wrapper {
      & > *:first-child {
        width: 0;
      }

      & > *:last-child {
        width: 100%;
      }
    }
  }
}
</style>
