<template lang="pug">
div
  div(class="swiper")
    div(class="swiper-wrapper")
      div(class="swiper-slide")
        v-col
          v-row(class="swiper-slide-content")
            v-card(class="card" color="transparent" min-height="320" width="200")
            v-card(class="card" color="transparent" min-height="320" width="200")
            v-card(class="card" color="transparent" min-height="320" width="200")
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
      mobile: false,
      laptop: false,
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
}

.swiper-slide-content {
  justify-content: center;
  gap: 25px;
}
</style>
