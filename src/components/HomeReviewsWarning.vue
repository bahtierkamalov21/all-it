<template lang="pug">
div(v-if="!this.$store.state.user")
  v-card(class="card rounded-lg pa-4 pt-2 pb-6 mt-6")
    div(class="card-bottom")
    div(class="card-top")
    div(class="d-flex flex-wrap align-center mt-5" style="gap: 6px")
      v-card(class="warning-bottom text-subtitle-1 font-weight-bold pa-2 px-4")
        | Чтобы оставить отзыв вам требуется 
      v-btn(
        @click="$router.push('/profile')"
        color="costumBlue"
        class="warning-bottom font-weight-bold text-capitalize white--text pa-2"
      )
        | Войти
</template>

<script>
export default {
  name: "HomeReviewsWarning",
};
</script>

<style scoped lang="scss">
.card {
  box-shadow: var(--shadow-2xl) !important;
  overflow: hidden;
  position: relative;

  &-bottom {
    height: 15px;
    width: 100%;
    position: absolute;
    bottom: 0;
    left: 0;
    border-radius: 0 !important;
    background: #1976d2;
    animation: background 4s infinite alternate;
  }

  &-top {
    height: 18px;
    width: 80%;
    border-bottom-right-radius: 10px;
    top: 0;
    left: 0;
    position: absolute;
    background: #1976d2;
    animation: background 4s infinite;
  }
}

.warning-bottom {
  border-radius: 5px !important;
  line-height: 20px !important;
  box-shadow: var(--shadow-lg) !important;
}

@keyframes background {
  50% {
    background: darkviolet;
    box-shadow: 0 -140px 70px -120px mediumorchid inset,
      0 -210px 70px -120px teal inset 0 -280px 70px -120px plum inset;
  }
}
</style>
