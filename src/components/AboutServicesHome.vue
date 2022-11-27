<template lang="pug">
div
  section(class="about-services")
    v-container
      div(class="swiper")
        div(class="swiper-wrapper")
          div(class="swiper-slide")
        div(class="swiper-pagination")
</template>

<script>
import Swiper from "swiper";
import "swiper/css";
import "swiper/css/pagination";

export default {
  name: "AboutServicesHome",
  data() {
    return {
      swiper: null,
    };
  },
  mounted() {
    this.swiper = new Swiper(".swiper", {
      pagination: {
        el: ".swiper-pagination",
      },
    });
  },
};
</script>

<style scoped lang="scss">
.about-services {
  background-color: #323232;
  box-shadow: 0 0 24px 4px rgba(0, 0, 0, 0.6);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-image: url("../assets/images/services-background.jpg");
}
</style>
