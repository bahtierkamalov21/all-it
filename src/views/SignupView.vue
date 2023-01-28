<template lang="pug">
div
  header(class="header pb-12")
    v-container
      v-card(class="card text-center mx-auto pa-6 rounded-xl" max-width="420")
        v-chip(color="costumBlue")
          router-link(to="signin" class="text-decoration-none font-weight-bold white--text") Войти?
        h1(class="text-center") Регистрация
        sign-complete(v-if="complete")
        v-form(v-else ref="form" class="mt-6" v-model="valid" lazy-validation @submit.prevent="registration")
          v-text-field(
            v-model="first_name" 
            label="Имя"
            solo
            class="input"
          )
          v-text-field(
            v-model="last_name" 
            solo
            class="input" 
            label="Фамилия"
          )
          v-text-field(
            v-model="username" 
            required
            label="Имя пользователя" 
            :rules="[v => !!v || 'Имя пользователя обязательно']"
            :error-messages="error"
            solo
            class="input"
            @input="changeInput"
          )
          v-text-field(
            v-model="password" 
            :rules="passwordRules" 
            label="Пароль"
            solo
            class="input"
          )
          v-text-field(
            v-model="telegramUsername" 
            label="Telegram username" 
            solo
            class="input"
            :error-messages="errorTelegram"
            :rules="telegramUsernameRules"
            @input="changeInput"
          )
          v-text-field(
            v-model="email" 
            label="Email" 
            solo
            class="input"
            :error-messages="errorEmail"
            :rules="emailRules"
            @input="changeInput"
          )
          v-text-field(
            v-model="phone" 
            label="Телефон"
            required
            solo
            class="input"
            :error-messages="errorPhone"
            :rules="phoneRules"
            @input="changeInput"
          )
          v-btn(
            @click="registration" 
            class="white--text font-weight-bold text-capitalize mt-2" 
            elevation="0" 
            :disabled="!valid" 
            rounded 
            color="costumBlue"
          ) Зарегистрироваться
</template>

<script>
import axios from "axios";
import decodedTokensAndSetUserData from "@/mixins/decodedTokensAndSetUserData";
import SignComplete from "@/components/SignComplete";

export default {
  name: "SignupView",
  data() {
    return {
      valid: false,
      first_name: null,
      last_name: null,
      complete: false,
      username: null,
      password: null,
      telegramUsername: null,
      errorEmail: null,
      phone: null,
      email: null,
      emailRules: [
        (v) => !!v || "Email обязателен",
        (v) => /.+@.+\..+/.test(v) || "Не корректный email",
      ],
      error: null,
      errorPhone: null,
      errorTelegram: null,
      phone_regex: /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/,
      phoneRules: [
        (v) => this.phone_regex.test(v) || "Неверно введен номер телефона",
      ],
      password_regex: /^[a-zA-Z0-9]{6,}/,
      passwordRules: [
        (v) => !!v || "Пароль обязателен",
        (v) =>
          this.password_regex.test(v) ||
          "Пароль должен состоять из 6 цифр и латинских букв",
      ],
      telegram_username_regex: /^@[A-Za-z\d_]{2,32}$/,
      telegramUsernameRules: [
        (v) => {
          if (!v) return true;
          return (
            this.telegram_username_regex.test(v) ||
            "Неверно введен telegram username"
          );
        },
      ],
    };
  },
  components: { SignComplete },
  mixins: [decodedTokensAndSetUserData],
  created() {
    localStorage.getItem("user") ? this.$router.push("/") : null;
  },
  mounted() {
    window.scrollTo(0, 0);
  },
  methods: {
    changeInput() {
      this.error = null;
      this.errorPhone = null;
      this.errorTelegram = null;
    },
    registration() {
      if (this.$refs.form.validate()) {
        axios
          .post(this.$store.state.api_url + "users/", {
            firts_name: this.first_name,
            last_name: this.last_name,
            username: this.username,
            password: this.password,
            telegram_username: this.telegramUsername,
            email: this.email,
            phone: this.phone,
            is_active: true,
          })
          .then(() => {
            // Сохраняем username и passowrd в localStorage
            localStorage.setItem("username", this.username);
            localStorage.setItem("password", this.password);
            // Сохраняем username и passowrd в store
            this.$store.commit("setUsername", this.username);
            this.$store.commit("setPassword", this.password);

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
            } else if (errors.response.data.phone) {
              this.errorPhone = errors.response.data.phone;
            } else if (errors.response.data.telegram_username) {
              this.errorTelegram = errors.response.data.telegram_username;
            } else if (errors.response.data.email) {
              this.errorEmail = errors.response.data.email;
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
  background-image: url("../assets/images/about-background.png");
  background-repeat: no-repeat;
  background-size: cover;
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
