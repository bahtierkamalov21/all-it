<template lang="pug">
div
  div(class="swiper")
    div(class="swiper-wrapper")
      div(class="swiper-slide")
        v-col(class="pa-0 pt-4 pb-4")
          v-row(class="swiper-slide-content")
            v-card(
              v-for="service in services"
              :key="service.id"
              class="card pa-8"
              color="transparent rounded-lg"
              min-height="320"
              max-width="240"
            )
              v-icon(:color="service.icon_color") {{ "mdi-" + service.icon }}
              h3(class="mt-2") {{ service.title }}
              p(class="mt-2") {{ service.text }}
    div(class="swiper-pagination")
</template>

<script>
import { Swiper, Pagination } from "swiper";
import "swiper/css";
import "swiper/css/pagination";

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
      modules: [Pagination],
      pagination: {
        el: ".swiper-pagination",
      },
    });
  },
};
</script>

<style scoped lang="scss">
.card {
  border: 1px solid #ffffff !important;
  background-color: rgba(255, 255, 255, 0.012) !important;
  color: #ffffff;
  box-shadow: var(--shadow-2xl) !important;

  & > .v-icon {
    font-size: 6rem;
  }

  & > p {
    opacity: 0.8;
  }
}

.swiper-slide-content {
  justify-content: center;
  gap: 25px;
}
</style>
