<template lang="pug">
div
  section(class="reviews py-16")
    v-container(class="pt-10 px-6")
      h2(class="mb-4") Отзывы
      v-col
        v-row(class="justify-space-between")
          div(class="left")
            h3 Справа мы оставляем популярные и недавние отзывы
            h4 Больше 5 лет мы успешно работаем с крупными брендами со всего мира
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
                  div(class="swiper-slide" v-for="item in reviews" :key="item.id")
                    v-col 
                      v-row(class="align-center justify-space-between")
                        v-list
                          v-list-item
                            v-list-item-avatar
                              v-img(v-if="item.fk_user.avatar" :src="item.fk_user.avatar")
                              v-icon(v-else style="font-size: 48px;") mdi-account-circle
                            v-list-item-content
                              v-list-item-title {{ item.fk_user.first_name ? item.fk_user.first_name : item.fk_user.username }}
                              v-list-item-subtitle {{ item.fk_user.last_name }}
                        div(class="d-flex align-center pr-12")
                          v-icon(color="yellow" v-for="rating in item.rating") mdi-star-shooting 
                          //- | {{ for(let i = 0; i < item.rating; i++) { return v-icon(color="yellow") mdi-star-shooting } }}
                          v-chip(color="primary" class="ml-2") Рейтинг
                    div(class="swiper-slide-message px-4") {{ item.message }}
</template>

<script>
import axios from "axios";
import Swiper from "swiper";

export default {
  name: "HomeReviews",
  data() {
    return {
      swiperReviews: null,
      reviews: [],
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
  created() {
    this.getReviews();
  },
  mounted() {
    this.swiperReviews = new Swiper(".swiper-reviews");
    console.log(this.swiperReviews);
  },
  methods: {
    getReviews() {
      axios
        .get(this.$store.state.api_url + "populars_reviews/")
        .then((response) => {
          const reviews = response.data;
          reviews.forEach((item) => {
            axios
              .get(item.fk_user_review)
              .then((response) => {
                let fk_user_review = response.data;
                axios
                  .get(response.data.fk_user)
                  .then((response) => {
                    fk_user_review.fk_user = {
                      first_name: response.data.first_name,
                      last_name: response.data.last_name,
                      username: response.data.username,
                      avatar: response.data.avatar,
                    };
                    this.reviews.push(fk_user_review);
                  })
                  .catch((errors) => {
                    console.log(errors);
                  });
              })
              .catch((errors) => {
                console.log(errors);
              });
          });
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
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

.left {
  width: 50%;
  padding-right: 12px;
}

.card {
  overflow: hidden;
  box-shadow: var(--shadow-2xl) !important;
}

.swiper-slide {
  &-message {
    max-height: 234px;
    overflow: auto;
  }
}

@media screen and (max-width: 600px) {
  .reviews {
    padding-top: 112px !important;
  }
  .right {
    width: 100%;
  }
}
</style>
