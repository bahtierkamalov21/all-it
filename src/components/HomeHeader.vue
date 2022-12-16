<template lang="pug">
div
  div(class="header")
    div(class="header-wrapper" ref="headerWrapper")
      div
      div
        shapes-home-header
    v-container(class="header-container" ref="headerContainer")
      div(class="top")
        v-col 
          v-row(class="align-center") 
            div(class="left d-flex flex-column")
              v-chip(color="primary" style="width: fit-content;")
                v-icon(class="status mr-2") mdi-star-check
                | Frontend Backend | Web Developers
              h1(class="the-title") {{ $t("header__h1") }}
              h2(class="pa-0 font-weight-medium")
                | {{ $t("modern") }}
                br
                | {{ $t("projects") }}
                v-chip(color="costumBlue" class="ml-4 rounded-xl")
                  | WCAG 3.0
              v-btn(
                class="text-capitalize white--text mt-8"
                rounded 
                color="costumBlue"
                elevation="0"
                x-large
                width="250"
              )
                font-awesome-icon(icon="fa-solid fa-layer-group" class="mr-2")
                | {{ $t("discuss") }}
                span(class="ml-1 text-lowercase") {{ $t("project") }}
            div(class="right")
      div(class="bottom mt-6")
        marquee-item
</template>

<script>
import ShapesHomeHeader from "./ShapesHomeHeader.vue";
import MarqueeItem from "./MarqueeItem";
import { mapState } from "vuex";

export default {
  name: "HomeHeader",
  components: { ShapesHomeHeader, MarqueeItem },
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
        this.$refs.headerContainer.style.backgroundColor = "#262626D9";
      } else {
        this.$refs.headerContainer.style.backgroundColor =
          "rgba(255, 255, 255, 0.6)";
      }
    },
    changeStopIntervalShapes(data) {
      this.stopIntervalShapes = data;
    },
    changeStyleElementsForMedia() {
      this.$refs.headerWrapper.style.minHeight = `${
        this.$refs.headerContainer.offsetHeight + 198
      }px`;
    },
  },
  mounted() {
    // If default dark theme
    this.changeBackgroundContainer();
    // First initilization media styles
    this.changeStyleElementsForMedia();
    // Resize window
    window.addEventListener("resize", () => {
      this.changeStyleElementsForMedia();
    });
  },
};
</script>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
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
      min-height: inherit;
      position: relative;
    }
  }

  &-container {
    position: absolute;
    backdrop-filter: blur(12px);
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 12px;
    box-shadow: var(--shadow-lg);
    padding: 32px;
    padding-bottom: 26px;
    top: 112px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    transition: all 0.2s ease-in-out;
  }
}

.left {
  width: 100%;
}

.the-title {
  font-size: var(--size-title);
}

.bottom {
  padding-top: auto;
}

h2 {
  font-size: calc(var(--index) * 2.8);
  padding: 10px;
  padding-right: 20px;
  line-height: calc(var(--index) * 2.8);
  display: inline-block;

  & > *:last-child {
    font-size: calc(var(--index) * 1.2);
    padding: calc(var(--index) * 1.2);
    color: #ffffff;
  }
}

@media screen and (max-width: 1086px) {
  .header {
    &-container {
      width: 92.2%;
    }
  }
}

@media screen and (max-width: 600px) {
  .header {
    &-wrapper {
      & > *:first-child {
        width: 0;
      }

      & > *:last-child {
        width: 100%;
      }
    }

    &-container {
      padding: 18px;
      backdrop-filter: none;
    }
  }

  .h2 {
    font-size: calc(var(--index) * 2.8);
    line-height: 2.4rem;

    & > *:last-child {
      font-size: calc(var(--index) * 1.4);
      padding: calc(var(--index) * 1.2);
    }
  }

  .left {
    width: 100%;

    &-button {
      width: 232px !important;
      margin-top: 24px !important;
      font-size: 14px;
    }
  }
}
</style>
