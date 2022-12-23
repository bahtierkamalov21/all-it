<template lang="pug">
div
  div(class="header")
    div(class="header-wrapper" ref="headerWrapper")
      div
      div
        shapes-home-header
    v-container(class="header-container rounded-xl" ref="headerContainer")
      div(class="top")
        v-col 
          v-row(class="align-center") 
            div(class="left d-flex flex-column")
              v-chip(color="primary" class="pr-4" style="width: fit-content;")
                v-icon(class="status mr-2") mdi-star-check
                | Frontend Backend | Web Developers
              h1(class="the-title") {{ $t("header__h1") }}
              h2(class="pa-0")
                | {{ $t("modern") }}
                br
                | {{ $t("projects") }}
                v-chip(color="costumBlue" class="ml-2 rounded-xl")
                  | WCAG 3.0
              v-btn(
                class="text-capitalize font-weight-bold white--text mt-8"
                rounded 
                color="costumBlue"
                elevation="0"
                x-large
                width="312"
              )
                font-awesome-icon(icon="fa-solid fa-layer-group" class="mr-2")
                | Получить
                span(class="ml-1 text-lowercase") консультацию
            div(class="right")
      div(class="bottom mt-6")
        marquee-item
</template>

<script>
import ShapesHomeHeader from "./ShapesHomeHeader.vue";
import MarqueeItem from "./MarqueeItem";

export default {
  name: "HomeHeader",
  components: { ShapesHomeHeader, MarqueeItem },
  methods: {
    changeStyleElementsForMedia() {
      this.$refs.headerWrapper.style.minHeight = `${
        this.$refs.headerContainer.offsetHeight + 198
      }px`;
    },
  },
  mounted() {
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
    backdrop-filter: blur(16px);
    box-shadow: var(--shadow-2xl);
    padding: 32px;
    padding-bottom: 26px;
    top: 112px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
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
