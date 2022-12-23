<template lang="pug">
div
  v-card(class="card rounded-lg pa-4 pt-2 pb-6")
    div(class="card-bottom")
    div(class="text-right")
      div(class="card-top")
    p(class="font-weight-bold mb-2 mt-6" v-if="!this.$store.state.user")
      | Чтобы оставить отзыв вам требуется 
      router-link(to="/signin") войти
    div(class="warning-bottom white--text text-subtitle-1 font-weight-medium pa-2")
      | Оставить отзыв можно будет после
      br
      | завершения выполнения вашего проекта. 
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
  background-image: url("../assets/images/services-background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

@keyframes background {
  50% {
    background: darkviolet;
    box-shadow: 0 -140px 70px -120px mediumorchid inset,
      0 -210px 70px -120px teal inset 0 -280px 70px -120px plum inset;
  }
}
</style>
