<template lang="pug">
div(class="pt-16")
  v-main
    v-container
      v-text-field(v-model="username")
      v-text-field(v-model="password")
      v-btn(@click="signin") Зарегистрироваться
</template>

<script>
import axios from "axios";

export default {
  name: "SigninView",
  data() {
    return {
      username: null,
      password: null,
    };
  },
  methods: {
    signin() {
      axios
        .post(this.$store.state.api_url + "token/", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          localStorage.setItem("user", response.data);
          console.log(localStorage.getItem("user"));
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
  },
};
</script>
