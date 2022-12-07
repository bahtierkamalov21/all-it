<template lang="pug">
div
  section(class="reviews py-16")
    v-container(class="pt-10 px-6")
      h2 Отзывы
      v-col
        v-row(class="align-center justify-space-between")
          div(class="left")
            h2 Отзывы
          div(class="right")
            v-card(class="card py-4 rounded-lg" elevation="0")
              div(class="d-flex align-center justify-space-between px-4")
                div(class="font-weight-bold") Популярные отзывы
                div(class="card-buttons")
                  v-btn(
                    elevation="0" 
                    class="pa-0 mr-2" 
                    min-width="48" 
                    @click="swiperReviews.slidePrev()" 
                    :disabled="disabledPrevSlide"
                  )
                    v-icon mdi-arrow-left
                  v-btn(
                    elevation="0" 
                    class="pa-0" 
                    min-width="48" 
                    @click="swiperReviews.slideNext()" 
                    :disabled="disabledNextSlide"
                  )
                    v-icon mdi-arrow-right
              div(class="swiper-reviews")
                div(class="swiper-wrapper")
                  div(class="swiper-slide")
                    div(class="px-4") dcdcs
                  div(class="swiper-slide")
                    div(class="px-4")
                      | cascasca
</template>

<script>
import Swiper from "swiper";

export default {
  name: "HomeReviews",
  data() {
    return {
      swiperReviews: null,
    };
  },
  computed: {
    disabledPrevSlide() {
      if (this.swiperReviews) {
        return this.swiperReviews.activeIndex === 0;
      } else return null;
    },
    disabledNextSlide() {
      if (this.swiperReviews) {
        if (
          this.swiperReviews.activeIndex ===
          this.swiperReviews.slides.length - 1
        ) {
          return true;
        } else return false;
      } else return null;
    },
  },
  mounted() {
    this.swiperReviews = new Swiper(".swiper-reviews");
    console.log(this.swiperReviews);
  },
};
</script>

<style scoped lang="scss">
.reviews {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.4);

  & > div {
    background-color: transparent !important;
  }
}

h2 {
  font-size: var(--section-title);
}

.right {
  width: 50%;
}

.card {
  overflow: hidden;
  box-shadow: var(--shadow-2xl) !important;
}
</style>
