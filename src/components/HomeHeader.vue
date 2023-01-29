<template lang="pug">
div
  div(class="header")
    div(class="header-wrapper")
      div
      div
        shapes-home-header
    v-container(class="header-container rounded-xl")
      div(class="top")
        v-col 
          v-row(class="align-center") 
            div(class="left d-flex flex-column")
              v-chip(color="primary" class="pr-4 mb-4 chip font-weight-bold" style="width: fit-content;")
                v-icon(class="status mr-2") mdi-star-check
                | Frontend Backend | Web Developers
              h1 {{ $t("header__h1") }}
              h2(class="pa-0")
                | {{ $t("modern") }}
                br
                | {{ $t("projects") }}
                v-chip(color="costumBlue" class="ml-2 white--text rounded-xl")
                  | WCAG 3.0
              v-btn(
                class="button-consultation text-capitalize font-weight-bold white--text mt-8"
                rounded 
                color="costumBlue"
                elevation="0"
                x-large
                width="312"
              )
                font-awesome-icon(icon="fa-solid fa-layer-group" class="mr-2")
                | {{ $t("get-consultation") }}
                span(class="ml-1 text-lowercase") {{ $t("get-consultation2") }}
      div(class="bottom mt-6")
        marquee-item
</template>

<script>
import ShapesHomeHeader from "./ShapesHomeHeader.vue";
import MarqueeItem from "./MarqueeItem";

export default {
  name: "HomeHeader",
  components: { ShapesHomeHeader, MarqueeItem },
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
    max-width: 1160px;
    display: flex;
    align-items: center;
    height: 600px;

    & > *:first-child {
      width: 50%;
      height: 100%;
    }

    & > *:last-child {
      width: 50%;
      height: 100%;
      min-height: inherit;
      position: relative;
    }
  }

  &-container {
    position: absolute;
    backdrop-filter: blur(16px);
    box-shadow: var(--shadow-2xl), 0 0 24px 0 rgba(255, 255, 255, 0.2) inset;
    padding: 32px;
    padding-bottom: 26px;
    width: 95%;
    top: 112px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
  }
}

.bottom {
  padding-top: auto;
}

h2 {
  padding: 10px;
  padding-right: 20px;
  display: inline-block;

  & > *:last-child {
  }
}

@media screen and (max-width: 1086px) {
  .header {
    &-wrapper {
      height: 590px;
    }

    &-container {
      width: 92.2%;
    }
  }
}

@media screen and (max-width: 600px) {
  .header {
    &-wrapper {
      height: 540px;

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

  .chip {
    font-size: 12px !important;
  }

  h2 {
    font-size: calc(var(--index) * 2.8);
    line-height: 2.4rem;

    & > *:last-child {
      font-size: calc(var(--index) * 1.4);
      padding: calc(var(--index) * 1.2);
    }
  }

  .button-consultation {
    margin-top: 24px !important;
  }
}
</style>
