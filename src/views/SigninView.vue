<template lang="pug">
div
  header(class="header pb-12")
    v-container
      div(style="max-width: 420px; margin: auto;")
        v-card(class="card text-center mx-auto pa-6 rounded-xl")
          v-chip(color="costumBlue")
            router-link(to="signup" class="text-decoration-none font-weight-bold white--text") Зарегистрироваться?
          h1 Login
          sign-complete(v-if="complete")
          v-form(v-else ref="form" class="mt-6" v-model="valid" lazy-validation @submit.prevent="signin")
            div(v-if="loginToPhone")
              v-text-field(
                v-model="phone" 
                label="Номер телефона"
                solo
                @input="changeInput"
                :rules="phoneRules"
                class="input"
                :error-messages="error"
                autocomplete="phone"
              )
              v-text-field(
                v-model="password" 
                label="Пароль"
                :rules="passwordRules"
                solo
                @input="changeInput"
                class="input"
                :error-messages="error"
                autocomplete="current-password"
              )
            div(v-else)
              v-text-field(
                v-model="username" 
                label="Имя пользователя"
                :rules="[(v) => !!v || 'Имя пользователя обязательно']"
                solo
                @input="changeInput"
                class="input"
                :error-messages="error"
                autocomplete="username"
              )
              v-text-field(
                v-model="password" 
                label="Пароль"
                :rules="passwordRules"
                solo
                @input="changeInput"
                class="input"
                :error-messages="error"
                autocomplete="current-password"
              )
            div(class="text-left mb-4")
              v-btn(
                style="font-size: 12px !important;"
                class="text-capitalize font-weight-bold white--text"
                rounded 
                @click="loginToPhone = true"
                color="costumBlue"
                elevation="0"
                v-if="!loginToPhone"
              )
                | Войти
                span(class="text-lowercase mx-1") по
                span(class="text-lowercase mr-1") номеру
                span(class="text-lowercase") телефона
              v-btn(
                style="font-size: 12px !important;"
                class="text-capitalize font-weight-bold white--text"
                rounded 
                @click="loginToPhone = false"
                color="costumBlue"
                elevation="0"
                v-else
              )
                | Войти
                span(class="text-lowercase mx-1") по
                span(class="text-lowercase mr-1") имени
                span(class="text-lowercase") пользователя
            v-btn(
              @click="signin" 
              class="white--text font-weight-bold text-capitalize mt-2" 
              elevation="0" 
              :disabled="!valid" 
              rounded 
              color="costumBlue"
            ) Войти
        v-btn(
          v-if="false"
          style="font-size: 12px !important;"
          class="text-capitalize font-weight-bold white--text mt-2 ml-6"
          rounded 
          elevation="0"
          color="costumBlue"
          @click="$router.push('/restore')"
        ) Забыли
          span(class="ml-1 text-lowercase") пароль?
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
      phone: null,
      loginToPhone: false,
      error: null,
      valid: false,
      phone_regex: /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/,
      phoneRules: [
        (v) => this.phone_regex.test(v) || "Неверно введен номер телефона",
      ],
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
    localStorage.getItem("user") ? this.$router.push("/") : null;
  },
  methods: {
    signin() {
      if (this.$refs.form.validate()) {
        if (this.loginToPhone) {
          // Отправляем запрос на api, чтобы получить username
          axios
            .get(this.$store.state.api_url + "username_phone_number/", {
              params: {
                phone: this.phone,
                password: this.password,
              },
            })
            .then((response) => {
              // Получаем токены
              axios
                .post(this.$store.state.api_url + "token/", {
                  username: response.data,
                  password: this.password,
                })
                .then((response) => {
                  // Сохраняем username и passowrd в localStorage
                  localStorage.setItem("username", this.username);
                  localStorage.setItem("password", this.password);
                  // Сохраняем username и passowrd в store
                  this.$store.commit("setUsername", this.username);
                  this.$store.commit("setPassword", this.password);

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
            });
        } else {
          // Получаем токены
          axios
            .post(this.$store.state.api_url + "token/", {
              username: this.username,
              password: this.password,
            })
            .then((response) => {
              // Сохраняем username и passowrd в localStorage
              localStorage.setItem("username", this.username);
              localStorage.setItem("password", this.password);
              // Сохраняем username и passowrd в store
              this.$store.commit("setUsername", this.username);
              this.$store.commit("setPassword", this.password);

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
      }
    },
    changeInput() {
      this.error = null;
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
  background-image: url("../assets/images/about-background.png");
  background-repeat: no-repeat;
  background-size: cover;
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

h1 {
  font-size: 38px;
  line-height: initial;
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
