<template lang="pug">
div
  v-dialog(hide-overlay v-model="dialogReviewsLocal" width="500")
    div
      div(class="title font-weight-bold pl-6 mb-2") Оставить отзыв
      v-card(class="card rounded-lg pa-6" elevation="0")
        v-form(ref="form" v-model="valid" lazy-validation @submit.prevent="postReview")
          div(class="mb-5")
            v-textarea(
              label="Текст" 
              :rules="[v => !!v || 'Поле должно быть заполнено']" 
              v-model="message" 
              class="input" 
              solo 
              hide-details
            )
          div(class="d-flex flex-wrap justify-space-between" style="gap: 16px;")
            div(class="d-flex align-center")
              v-chip(color="costumBlue" class="white--text font-weight-bold mr-2") Рейтинг
              div(class="rating")
                v-icon(v-for="item in ratings" ref="rating" :key="item" @click="setRating(item)") mdi-star
            v-btn(@click="postReview" elevation="0" color="costumBlue" class="white--text font-weight-bold text-capitalize") Добавить
        v-chip(v-if="error") {{ error }}
</template>

<script>
import axios from "axios";

export default {
  name: "DilaogReviews",
  props: {
    dialogReviews: Boolean,
  },
  data() {
    return {
      ratings: [5, 4, 3, 2, 1],
      rating: null,
      message: null,
      valid: false,
      error: null,
    };
  },
  computed: {
    dialogReviewsLocal: {
      get() {
        return this.dialogReviews;
      },
      set(value) {
        this.sendDialogReviews(value);
      },
    },
  },
  methods: {
    sendDialogReviews(value) {
      this.$emit("getDialogReviews", value);
    },
    sendHaveReviews() {
      this.$emit("getHaveReviews", true);
    },
    postReview() {
      if (this.rating) {
        const api = this.$store.state.api_url;
        const usernameForToken = localStorage.getItem("username");
        const passwordForToken = localStorage.getItem("password");

        axios
          .post(api + "token/", {
            username: usernameForToken,
            password: passwordForToken,
          })
          .then((response) => {
            // Сохраняем токены в localStorage
            localStorage.setItem("token_access", response.data.access);
            localStorage.setItem("token_refresh", response.data.refresh);
            // Сохраняем токены с store
            this.$store.commit("setTokenAccess", response.data.access);
            this.$store.commit("setTokenRefresh", response.data.refresh);

            const user = JSON.parse(localStorage.getItem("user"));

            // Сохраняем отзыв пользователя
            const data = {
              message: this.message,
              rating: this.rating,
              fk_user: user.url,
            };

            axios
              .post(api + "users_reviews/", data, {
                headers: {
                  Authorization: `Bearer ${this.$store.state.token_access}`,
                },
              })
              .then((response) => {
                // Url отзыва для добавления его в поле review пользователя
                const review_url = {
                  is_active: true,
                  phone: JSON.parse(localStorage.getItem("user")).phone,
                  password: JSON.parse(localStorage.getItem("user")).password,
                  telegram_username: JSON.parse(localStorage.getItem("user"))
                    .telegram_username,
                  username: JSON.parse(localStorage.getItem("user")).username,
                  review: response.data.url,
                };

                // Добавляем отзыв в модель пользователя
                const decoded = JSON.parse(localStorage.getItem("decoded"));
                axios
                  .put(api + `users/${decoded.user_id}/`, review_url, {
                    headers: {
                      Authorization: `Bearer ${this.$store.state.token_access}`,
                    },
                  })
                  .then(() => {
                    this.sendHaveReviews();
                    this.sendDialogReviews(!this.dialogReviews);
                  })
                  .catch((errors) => {
                    console.log(errors);
                  });
              })
              .catch((errors) => {
                console.log(errors);
              });
          })
          .catch((errors) => {
            console.log(errors);
          });
      } else {
        switch (this.$i18n.locale) {
          case "ru":
            this.error =
              "Для отправки отзыва нужно обязательно поставить рейтинг.";
            break;
          case "en":
            this.error = "To submit a review, you need to rate.";
            break;
          case "es":
            this.error = "Para enviar una reseña, debe calificar.";
            break;
        }
      }
    },
    setRating(data) {
      this.rating = data;
      this.$refs.rating.forEach((item) => {
        item.$el.classList.remove("active");
      });

      this.$refs.rating
        .slice()
        .reverse()
        .forEach((item, index) => {
          index <= data - 1 ? item.$el.classList.add("active") : null;
        });
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  box-shadow: var(--shadow-2xl) !important;
  overflow: hidden;
}

.title {
  color: #121133;
}

.rating {
  display: flex;
  align-items: center;
  gap: 4px;
  flex-direction: row-reverse;
  justify-content: flex-start;

  & > * {
    font-size: 24px !important;

    &:hover,
    &:hover ~ button {
      color: yellow !important;
    }
  }
}

.active {
  color: var(--custom-blue) !important;
}
</style>
