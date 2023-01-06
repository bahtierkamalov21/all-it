<template lang="pug">
div
  header(class="header pb-12")
    v-container
      v-card(class="card text-center mx-auto pa-6 rounded-xl" max-width="420")
        v-chip(color="costumBlue")
          router-link(to="signin" class="text-decoration-none font-weight-bold white--text") Войти?
        h1(class="text-center") Регистрация
        v-form(ref="form" v-model="valid" lazy-validation @submit.prevent="registration")
          v-text-field(v-model="first_name" rounded label="Имя")
          v-text-field(v-model="last_name" rounded label="Фамилия")
          v-text-field(
            v-model="username" 
            rounded 
            required
            label="Имя пользователя" 
            :rules="[v => !!v || 'Имя пользователя обязательно']"
            :error-messages="error"
            class="field-sign"
          )
          v-text-field(
            v-model="password" 
            :rules="passwordRules" 
            rounded label="Пароль"
            class="field-sign"
          )
          v-text-field(
            v-model="telegramUsername" 
            rounded 
            label="Telegram username" 
            required
            class="field-sign"
            :rules="telegramUsernameRules"
          )
          v-btn(@click="registration" class="white--text text-capitalize mt-6" elevation="0" :disabled="!valid" rounded color="costumBlue") Зарегистрироваться
</template>

<script>
import axios from "axios";
import decodedTokensAndSetUserData from "@/mixins/decodedTokensAndSetUserData";

export default {
  name: "SignupView",
  data() {
    return {
      valid: false,
      first_name: null,
      last_name: null,
      username: null,
      password: null,
      telegramUsername: null,
      error: null,
      password_regex: /^[a-zA-Z0-9]{6,}/,
      passwordRules: [
        (v) => !!v || "Пароль обязателен",
        (v) =>
          this.password_regex.test(v) ||
          "Пароль должен состоять из 6 цифр и латинских букв",
      ],
      telegram_username_regex: /^@[A-Za-z\d_]{5,32}$/,
      telegramUsernameRules: [
        (v) => !!v || "Telegram username обязателен",
        (v) =>
          this.telegram_username_regex.test(v) ||
          "Неверно введен telegram username",
      ],
    };
  },
  mixins: [decodedTokensAndSetUserData],
  created() {
    if (this.$store.state.user) {
      this.$router.push("/");
    }
  },
  mounted() {
    window.scrollTo(0, 0);
  },
  methods: {
    registration() {
      if (this.$refs.form.validate()) {
        axios
          .post(this.$store.state.api_url + "users/", {
            firts_name: this.first_name,
            last_name: this.last_name,
            username: this.username,
            password: this.password,
            telegram_username: this.telegramUsername,
          })
          .then(() => {
            // После создания пользователя
            axios
              .post(this.$store.state.api_url + "token/", {
                username: this.username,
                password: this.password,
              })
              .then((response) => {
                // Сохраняем токены в localStorage
                localStorage.setItem("token_access", response.data.access);
                localStorage.setItem("token_refresh", response.data.refresh);
                // Сохраняем токены с store
                this.$store.commit("setTokenAccess", response.data.access);
                this.$store.commit("setTokenRefresh", response.data.refresh);

                // Декодируем токен и получаем данные пользователя
                this.decodedTokensAndSetUserData();
              })
              .catch((errors) => {
                console.log(errors);
              });
          })
          .catch((errors) => {
            console.log(errors);
            if (errors.response.data.username) {
              this.error = errors.response.data.username;
            }
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
    right: -20px;
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
