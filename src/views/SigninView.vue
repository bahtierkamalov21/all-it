<template lang="pug">
div
  header(class="header pb-12")
    v-container
      v-card(class="card text-center mx-auto pa-6 rounded-xl" max-width="420")
        v-chip(color="costumBlue")
          router-link(to="signup" class="text-decoration-none font-weight-bold white--text") Зарегистрироваться?
        h1 Login
        v-form(ref="form" v-model="valid" lazy-validation @submit.prevent="signin")
          v-text-field(
            v-model="username" 
            class="field-sign"
            label="Имя пользователя"
            :rules="[(v) => !!v || 'Имя пользователя обязательно']"
            rounded
          )
          v-text-field(
            v-model="password" 
            label="Пароль"
            :rules="passwordRules"
            class="field-sign"
            rounded
          )
          v-btn(@click="signin" class="white--text text-capitalize mt-6" elevation="0" :disabled="!valid" rounded color="costumBlue") Войти
</template>

<script>
import axios from "axios";

export default {
  name: "SigninView",
  data() {
    return {
      username: null,
      password: null,
      valid: false,
      regex: /^[a-zA-Z0-9]{6,}/,
      passwordRules: [
        (v) => !!v || "Пароль обязателен",
        (v) =>
          this.regex.test(v) ||
          "Пароль должен состоять из 6 цифр и латинских букв",
      ],
    };
  },
  created() {
    if (this.$store.state.user) {
      this.$router.push("/");
    }
  },
  methods: {
    signin() {
      if (this.$refs.form.validate()) {
        axios
          .post(this.$store.state.api_url + "token/", {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            // Сохраняем данные в localStorage
            localStorage.setItem("tokens", response.data);
            localStorage.setItem("user", response.data.access);
            // Сохраняем данные с store
            this.$store.commit("setUser", response.data.access);
            this.$store.commit("setTokenAccess", response.data.access);
            this.$store.commit("setTokenRefresh", response.data.refresh);
            location.reload();
          })
          .catch((errors) => {
            console.log(errors);
          });
      }
    },
  },
};
</script>

<style scoped lang="scss">
.header {
  padding-top: 126px;
}

.card {
  box-shadow: var(--shadow-2xl) !important;
  position: relative;

  & > *:first-child {
    position: absolute;
    right: -90px;
    top: 20px;
  }
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}

@media screen and (max-width: 600px) {
  .card {
    & > *:first-child {
      position: absolute;
      right: 20px;
      top: -20px;
    }
  }
}
</style>
