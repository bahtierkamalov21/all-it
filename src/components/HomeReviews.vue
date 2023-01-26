<template lang="pug">
div
  section(class="reviews py-16" id="reviews")
    v-container(class="pt-10 px-6")
      v-col(class="mb-4")
        v-row(class="align-center justify-space-between")
          h2(class="align-center") Отзывы 
          v-chip(class="title-chip white--text font-weight-bold pa-2 px-4") Спасибо за вашу поддержку!
      v-col
        v-row(class="justify-space-between" style="gap: 12px;")
          div(class="left")
            v-card(class="card rounded-lg pa-4 mb-4")
              div(class="font-weight-bold") Мы ценим мнение наших клиентов и рады
                br
                | услышать обратную связь
            home-reviews-warning
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
                    div(class="d-flex flex-wrap reviews-top align-center justify-space-between")
                      v-list
                        v-list-item
                          v-list-item-avatar
                            v-img(v-if="item.fk_user.avatar" :src="item.fk_user.avatar")
                            v-icon(v-else style="font-size: 48px;") mdi-account-circle
                          v-list-item-content(class="pl-0")
                            v-list-item-title {{ item.fk_user.first_name ? item.fk_user.first_name : item.fk_user.username }}
                            v-list-item-subtitle {{ item.fk_user.last_name }}
                      div(class="d-flex align-center pr-6")
                        v-icon(color="yellow" v-for="rating in item.rating" :key="rating.id") mdi-star
                        //- | {{ for(let i = 0; i < item.rating; i++) { return v-icon(color="yellow") mdi-star-shooting } }}
                        v-chip(color="primary" class="font-weight-bold px-4 ml-2") Рейтинг
                    div(class="swiper-slide-message px-4") {{ item.message }}
</template>

<script>
import HomeReviewsWarning from "@/components/HomeReviewsWarning";
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
  components: { HomeReviewsWarning },
  computed: {
    disabledPrevSlide() {
      return this.swiperReviews ? this.swiperReviews.activeIndex === 0 : null;
    },
    disabledNextSlide() {
      if (this.swiperReviews) {
        return this.swiperReviews.activeIndex ===
          this.swiperReviews.slides.length - 1
          ? true
          : false;
      } else return null;
    },
  },
  created() {
    this.getReviews();
  },
  mounted() {
    this.swiperReviews = new Swiper(".swiper-reviews");
  },
  methods: {
    async getReviews() {
      await axios
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

.left {
  flex-grow: 1;
}

.right {
  flex-grow: 2;
  width: calc(100vw / 2.5);
}

.title-chip {
  background-color: var(--custom-blue) !important;
}

.card {
  overflow: hidden;
  box-shadow: var(--shadow-2xl) !important;
}

.swiper-slide {
  overflow: hidden;

  &-message {
    max-height: 234px;
    overflow: auto;
    padding: 16px 0 0;
    font-weight: bold;
    box-shadow: 0 0 10px 0 rgb(0 0 0 / 20%);
  }
}

@media screen and (max-width: 600px) {
  .reviews {
    padding-top: 112px !important;

    &-top {
      & > *:last-child {
        margin-left: auto;
        margin-bottom: 20px;
      }
    }
  }
}
</style>
