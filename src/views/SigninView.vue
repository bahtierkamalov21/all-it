<template lang="pug">
div
  header(class="header pb-12")
    v-container
      v-card(class="card text-center mx-auto pa-6 rounded-xl" max-width="420")
        v-chip(color="costumBlue")
          router-link(to="signup" class="text-decoration-none font-weight-bold white--text") Зарегистрироваться?
        h1 Login
        sign-complete(v-if="complete")
        v-form(v-else ref="form" class="mt-6" v-model="valid" lazy-validation @submit.prevent="signin")
          v-text-field(
            v-model="username" 
            label="Имя пользователя"
            :rules="[(v) => !!v || 'Имя пользователя обязательно']"
            solo
            class="input"
            :error-messages="error"
          )
          v-text-field(
            v-model="password" 
            label="Пароль"
            :rules="passwordRules"
            solo
            class="input"
            :error-messages="error"
          )
          v-btn(@click="signin" class="white--text text-capitalize mt-2" elevation="0" :disabled="!valid" rounded color="costumBlue") Войти
</template>

<script>
import axios from "axios";
import decodedTokensAndSetUserData from "@/mixins/decodedTokensAndSetUserData";
import SignComplete from "@/components/SignComplete";

export default {
  name: "SigninView",
  data() {
    return {
      complete: false,
      username: null,
      password: null,
      error: null,
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
  components: { SignComplete },
  mixins: [decodedTokensAndSetUserData],
  created() {
    if (this.$store.state.user) {
      this.$router.push("/");
    }
  },
  methods: {
    signin() {
      if (this.$refs.form.validate()) {
        // Получаем токены
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
          .catch(() => {
            this.error = "Данные введены не верно";
          });
      }
    },
  },
  mounted() {
    window.scrollTo(0, 0);
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
