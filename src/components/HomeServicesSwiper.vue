<template lang="pug">
div
  div(class="swiper" style="max-width: 980px")
    div(class="swiper-wrapper")
      div(class="swiper-slide d-flex justify-center" v-for="service in services" :key="service.id")
        v-card(
          class="card white--text pa-8"
          color="transparent rounded-lg"
          min-height="320"
          max-width="240"
        )
          v-icon(:color="service.icon_color") {{ "mdi-" + service.icon }}
          h3(class="mt-2") {{ service.title }}
          p(class="mt-2") {{ service.text }}
  v-chip(color="prompt costumBlue white--text pr-4 mt-6")
    v-icon(class="mr-2") mdi-credit-card-fast-outline
    | Свайпните слайд
</template>

<script>
import { Swiper } from "swiper";

export default {
  name: "HomeServicesSwiper",
  data() {
    return {
      swiper: null,
      services: [
        {
          icon: "microsoft-visual-studio-code",
          icon_color: "#1e87f0",
          title: "Frontend & Backend",
          text:
            "Опыт наших коллег, партнеров и специалистов" +
            " позволяет реализовывать, задачи любого типа и сложности" +
            " за исключением программирования физического оборудования",
        },
        {
          icon: "language-python",
          icon_color: "#ffffff",
          title: "Frontend & Backend",
          text:
            "Опыт наших коллег, партнеров и специалистов" +
            " позволяет реализовывать, задачи любого типа и сложности" +
            " за исключением программирования физического оборудования",
        },
        {
          icon: "monitor-cellphone-star",
          icon_color: "#ffffff",
          title: "Frontend & Backend",
          text:
            "Опыт наших коллег, партнеров и специалистов" +
            " позволяет реализовывать, задачи любого типа и сложности" +
            " за исключением программирования физического оборудования",
        },
      ],
    };
  },
  mounted() {
    this.swiper = new Swiper(".swiper", {
      slidesPerView: 3,
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        640: {
          slidesPerView: 2,
        },
        1086: {
          slidesPerView: 3,
        },
      },
    });
  },
};
</script>

<style scoped lang="scss">
.card {
  border: 1px solid #ffffff !important;
  background-color: rgba(255, 255, 255, 0.012) !important;
  box-shadow: var(--shadow-2xl) !important;

  & > .v-icon {
    font-size: 6rem;
  }

  & > div {
    opacity: 0.8;
  }
}

.prompt {
  display: none;
}

@media screen and (max-width: 1086px) {
  .prompt {
    display: inline-block;
  }

  .swiper {
    max-width: 660px !important;
  }
}
</style>
