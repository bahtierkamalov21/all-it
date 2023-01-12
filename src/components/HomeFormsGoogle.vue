<template lang="pug">
div
  v-col 
    v-row(class="container ma-0")
      div(class="left rounded-xl pa-12")
        v-btn(@click="") Сброс пароля
      div(class="right d-flex align-center justify-center")
        font-awesome-icon(
          icon="fa-brands fa-google"
          class="right-icon"
        )
</template>

<script>
import axios from "axios";

export default {
  name: "HomeFormsGoogle",
  methods: {
    resetPassword() {
      axios
        .post(this.$store.state.api_url + "reset_password/", {
          email: "bakhtiyorkamalov21@gmail.com",
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
  },
};
</script>

<style scoped lang="scss">
.right {
  position: relative;
  flex-grow: inherit;

  &-icon {
    font-size: calc(var(--section-title) * 3);
  }
}
</style>
