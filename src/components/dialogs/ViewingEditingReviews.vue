<template lang="pug">
div
  v-dialog(v-model="accessDelete" hide-overlay width="440")
    v-card(
      class="card d-flex flex-column align-center justify-center pa-6 text-center rounded-xl" 
      style="gap: 12px;" 
      height="320" 
      width="100%"
    )
      div(class="title font-weight-bold") Вы точно хотите удалить ваш отзыв?
      v-icon(color="red" style="font-size: calc(var(--index) * 6);") mdi-delete
      div(class="d-flex" style="gap: 12px;")
        v-btn(
          class="text-capitalize font-weight-bold white--text" 
          color="red" 
          elevation="0"
          @click="deleteReview"
        ) Удалить
        v-btn(
          class="text-capitalize font-weight-bold" 
          elevation="0" 
          @click="setAccessDelete('close')"
        ) Отмена
  v-dialog(v-model="dialogViewingEditingReviewsLocal" hide-overlay width="600")
    div(class="d-flex align-center flex-wrap justify-space-between navbar pl-6 pr-2 mb-2")
      div(class="title font-weight-bold") Мой отзыв
      div(class="d-flex align-center" v-if="review")
        v-btn(
          elevation="0"
          class="white--text text-capitalize mr-2"
          rounded 
          @click="editingReview = !editingReview" 
          v-if="editingReview" 
          color="costumBlue"
        )
          | Отмена
        v-btn(icon class="mr-2" @click="editingReview = !editingReview")
          v-icon mdi-cogs
        v-btn(icon color="red" @click="setAccessDelete('open')")
          v-icon mdi-delete
    v-card(class="card" elevation="0")
      loading-item(v-if="!review")
      div(v-else :class="editingReview ? 'text-center' : null")
        div(class="d-flex flex-wrap reviews-top align-center justify-space-between")
          v-list
            v-list-item
              v-list-item-avatar
                v-img(v-if="userDataAndLinkReview.avatar" :src="userDataAndLinkReview.avatar")
                v-icon(v-else style="font-size: 48px;") mdi-account-circle
              v-list-item-content(class="text-left pl-0")
                v-list-item-title {{ userDataAndLinkReview.first_name ? userDataAndLinkReview.first_name : userDataAndLinkReview.username }}
                v-list-item-subtitle {{ userDataAndLinkReview.last_name }}
          div(class="d-flex align-center pr-4")
            v-icon(color="yellow" v-for="rating in review.rating" :key="rating.id" v-if="!editingReview") mdi-star
            div(class="rating" v-if="editingReview")
              v-icon(v-for="item in ratings" ref="rating" :key="item" @click="setRating(item, true)") mdi-star
            v-chip(color="primary" class="font-weight-bold px-4 ml-2") Рейтинг
        div(class="message px-4" v-if="!editingReview") {{ review.message }}
        div(v-else class="pa-6 pb-4 pt-0")
          v-textarea(
            label="Текст" 
            :rules="[v => !!v || 'Поле должно быть заполнено']" 
            v-model="review.message" 
            outlined 
            class="input" 
            solo 
            @input="update = true"
            hide-details
          )
        v-btn(
          elevation="0"
          class="white--text mb-4 text-capitalize"
          rounded 
          :disabled="!update"
          v-if="editingReview" 
          @click="saveEditingReview"
          color="costumBlue"
        )
          | Сохранить
</template>

<script>
import axios from "axios";
import LoadingItem from "@/components/LoadingItem.vue";

export default {
  name: "ViewingEditingReviews",
  props: {
    dialogViewingEditingReviews: Boolean,
    userDataAndLinkReview: Object,
  },
  components: { LoadingItem },
  created() {
    this.userDataAndLinkReview.review ? this.getUserReview() : null;
  },
  watch: {
    dialogViewingEditingReviews() {
      this.userDataAndLinkReview.review ? this.getUserReview() : null;
    },
    accessDelete() {
      !this.accessDelete ? this.setAccessDelete("close") : null;
    },
    editingReview() {
      this.editingReview
        ? setTimeout(() => {
            this.setRating(this.review.rating, false);
          }, 60)
        : null;
    },
  },
  data: () => ({
    review: null,
    accessDelete: false,
    editingReview: false,
    ratings: [5, 4, 3, 2, 1],
    rating: null,
    update: false,
  }),
  computed: {
    dialogViewingEditingReviewsLocal: {
      get() {
        return this.dialogViewingEditingReviews;
      },
      set(value) {
        this.$emit("getDialogViewingEditingReviews", value);
      },
    },
  },
  methods: {
    saveEditingReview() {
      // Получаем токены
      axios
        .post(this.$store.state.api_url + "token/", {
          username: localStorage.getItem("username"),
          password: localStorage.getItem("password"),
        })
        .then((response) => {
          // Сохраняем токены в localStorage
          localStorage.setItem("token_access", response.data.access);
          localStorage.setItem("token_refresh", response.data.refresh);
          // Сохраняем токены с store
          this.$store.commit("setTokenAccess", response.data.access);
          this.$store.commit("setTokenRefresh", response.data.refresh);

          // Сохраняем изменения
          const user = JSON.parse(localStorage.getItem("user"));
          const data = {
            rating: this.rating,
            message: this.review.message,
            fk_user: user.url,
          };

          axios
            .put(this.userDataAndLinkReview.review, data, {
              headers: {
                Authorization: `Bearer ${this.$store.state.token_access}`,
              },
            })
            .then(() => {
              // Перезагружаем страницу во избежание оишбок
              location.reload();
            })
            .catch((errors) => {
              console.log(errors);
            });
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
    getUserReview() {
      axios.get(this.userDataAndLinkReview.review).then((response) => {
        this.review = {
          message: response.data.message,
          rating: response.data.rating,
        };
      });
    },
    setRating(data, click) {
      click ? (this.update = true) : null;

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
    setAccessDelete(method) {
      // Делаем это во избежание рекурсии
      if (method === "open") {
        this.$emit("getDialogViewingEditingReviews", false);
        this.accessDelete = true;
      } else if (method === "close") {
        this.accessDelete = false;
        this.$emit("getDialogViewingEditingReviews", true);
      }
    },
    deleteReview() {
      // Получаем токены
      axios
        .post(this.$store.state.api_url + "token/", {
          username: localStorage.getItem("username"),
          password: localStorage.getItem("password"),
        })
        .then((response) => {
          // Сохраняем токены в localStorage
          localStorage.setItem("token_access", response.data.access);
          localStorage.setItem("token_refresh", response.data.refresh);
          // Сохраняем токены с store
          this.$store.commit("setTokenAccess", response.data.access);
          this.$store.commit("setTokenRefresh", response.data.refresh);

          // Удаляем отзыв
          axios
            .delete(this.userDataAndLinkReview.review, {
              headers: {
                Authorization: `Bearer ${this.$store.state.token_access}`,
              },
            })
            .then(() => {
              // У нас больше нет отзывов
              this.$emit("getHaveReviews", false);
              // Закрываем диалоговое окно
              this.accessDelete = false;
            })
            .catch((errors) => {
              console.log(errors);
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
.card {
  box-shadow: var(--shadow-2xl) !important;
  overflow: hidden;
}

.message {
  max-height: 234px;
  overflow: auto;
  padding: 16px;
  font-weight: bold;
  box-shadow: 0 0 10px 0 rgb(0 0 0 / 20%);
}

.rating {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
  justify-content: flex-start;

  & > * {
    &:hover,
    &:hover ~ button {
      color: var(--custom-blue) !important;
    }
  }
}

.title {
  color: #121133;
}

.active {
  color: var(--custom-blue) !important;
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

  .navbar {
    padding-left: 8px !important;
  }
}
</style>
