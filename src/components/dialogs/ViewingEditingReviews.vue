<template lang="pug">
div
  v-dialog(v-model="dialogViewingEditingReviewsLocal" hide-overlay width="600")
    v-card(class="card" elevation="0")
      loading-item(v-if="!review")
      div(v-else)
        div(class="d-flex flex-wrap reviews-top align-center justify-space-between")
          v-list
            v-list-item
              v-list-item-avatar
                v-img(v-if="userData.user.avatar" :src="userData.user.avatar")
                v-icon(v-else style="font-size: 48px;") mdi-account-circle
              v-list-item-content(class="pl-0")
                v-list-item-title {{ userData.user.first_name ? userData.user.first_name : userData.user.username }}
                v-list-item-subtitle {{ userData.user.last_name }}
          div(class="d-flex align-center pr-4")
            v-icon(color="yellow" v-for="rating in review.rating" :key="rating.id") mdi-star
            v-chip(color="primary" class="font-weight-bold px-4 ml-2") Рейтинг
        div(class="swiper-slide-message px-4") {{ review.message }}
</template>

<script>
import axios from "axios";
import LoadingItem from "@/components/LoadingItem.vue";

export default {
  name: "ViewingEditingReviews",
  props: {
    dialogViewingEditingReviews: Boolean,
    userData: Object,
  },
  components: { LoadingItem },
  created() {
    this.getUserReview();
  },
  data: () => ({
    review: null,
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
    getUserReview() {
      axios.get(this.userData.linkReview).then((response) => {
        this.review = {
          message: response.data.message,
          rating: response.data.rating,
        };
      });
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  box-shadow: var(--shadow-2xl) !important;
}
</style>
