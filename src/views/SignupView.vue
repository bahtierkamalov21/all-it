<template lang="pug">
div(class="pt-16")
  v-main
    v-container
      v-text-field(v-model="username")
      v-text-field(v-model="password")
      v-text-field(v-model="telegramUsername")
      v-btn(@click="registration") Зарегистрироваться
</template>

<script>
import axios from "axios";

export default {
  name: "SignupView",
  data() {
    return {
      username: null,
      password: null,
      telegramUsername: null,
      error: null,
    };
  },
  methods: {
    registration() {
      axios
        .post(this.$store.state.api_url + "users/", {
          username: this.username,
          password: this.password,
          telegram_username: this.telegramUsername,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((errors) => {
          console.log(errors);
          if (errors.response.data.username) {
            this.error = errors.response.data.username;
          }
        });
    },
  },
};
</script>
