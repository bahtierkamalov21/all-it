<template lang="pug">
div
  v-main(class="main pb-16")
    v-container
      v-card(class="card d-flex flex-column pb-6 justify-center rounded-lg")
        h1(class="mb-8 text-center pt-8 px-6") {{ $t("page-not-found") }}
        v-chip(color="costumBlue" style="width: fit-content;" class="ma-auto font-weight-bold white--text rounded-xl") 404
        div(class="text mb-6 pa-6 pr-16 rounded-tr-xl rounded-br-xl white--text")
          div
            h2(class="mb-2") {{ $t("404-h2") }}
            div {{ $t("404-title") }}
            div {{ $t("404-subtitle") }}
        v-chip(color="costumBlue" class="not-found font-weight-bold white--text rounded-xl") 404
        div(class="d-flex justify-center align-center flex-wrap" style="gap: 12px;")
          v-btn(
            color="costumBlue white--text" 
            rounded 
            @click="$router.push('/')"
            elevation="0" 
            class="text-capitalize"
          )
            | {{ $t("on") }}
            span(class="text-lowercase ml-1") {{ $t("mains") }}
</template>

<script>
export default {
  name: "PageNotFound",
};
</script>

<style scoped lang="scss">
.main {
  padding-top: 126px !important;
  background-image: url("../assets/images/about-background.png");
  background-repeat: no-repeat;
  background-size: cover;
}

.card {
  box-shadow: var(--shadow-2xl) !important;
  position: relative;
  overflow: hidden;

  & > *:nth-child(2) {
    display: none;
  }
}

.not-found {
  position: absolute;
  right: 0;
  transform: rotate(90deg);
  font-size: calc(var(--index) * 2);
  padding: 2.2% 2%;
}

h1 {
  font-size: 38px;
  line-height: initial;
}

h2 {
  font-size: 28px;
  line-height: initial;
}

.text {
  display: flex;
  align-items: center;
  justify-content: right;
  width: 80%;
  background-color: var(--custom-blue);
  box-shadow: var(--shadow-2xl);
}

@media screen and (max-width: 1086px) {
  .main {
    padding-top: 106px;
  }
}

@media screen and (max-width: 600px) {
  .text {
    width: 95%;
    padding-right: 24px !important;
  }

  .not-found {
    display: none;
  }

  .card {
    & > *:nth-child(2) {
      font-size: 24px !important;
      padding: 20px 16px;
      margin-bottom: 24px !important;
    }

    & > *:first-child {
      margin-bottom: 24px !important;
    }
  }
}
</style>
