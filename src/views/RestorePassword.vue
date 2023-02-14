<template lang="pug">
div
  header(class="header pb-12")
    v-container
      div(style="max-width: 420px; margin: auto;")
        v-card(class="card text-center mx-auto pa-6 rounded-xl")
          h1 Восстановление
            br
            | пароля
          v-form(ref="form" class="mt-6" v-model="valid" lazy-validation @submit.prevent="signin")
            ul(class="d-flex flex-wrap step-ul pa-0")
              li(
                v-for="item in steps" 
                :key="item.id"
                class="step-step" 
                :class="{ 'active' : item.active }"
              )
                div 
                  span(v-if="!item.complete") {{ item.number }}
                  div(class="check-stage pb-1" v-if="item.complete")
                    v-img(src="../assets/icons/check-stage.svg")
                span {{ item.name }}
            v-card(class="mt-8" elevation="0")
              div(class="left-complete pa-12 pb-0" v-if="complete")
                v-icon(color="green") mdi-check-decagram
                v-card-text Ура, через 2 секунды станица будет перезагружена
              v-window(v-model="stage")
                v-window-item(:value="1")
                  div(class="font-weight-bold pl-4 text-left") Введите Email вашего аккаунта
                  v-text-field(
                    solo 
                    label="Email"
                    @input="changeInput"
                    class="input"
                    v-model="email"
                    :rules="emailRules"
                    :error-messages="errorEmail"
                  )
                v-window-item(:value="2")
                  div(class="font-weight-bold pl-4 text-left") Код отправлен вам на почту
                  div(class="ma-auto" style="max-width: 300px; position: relative;")
                    v-otp-input(
                      v-model="code"
                      :disabled="loading"
                      dark 
                      @input="changeInput"
                      length="4"
                      @finish="valid = true"
                    )
                      v-overlay(absolute :value="loading")
                        v-progress-circular(indeterminate color="primary")
                    div(class="text-left font-weight-bold red--text mb-4") {{ errorOtp }}
                    v-btn(@click="repeatCode" text class="text-capitalize mb-4" style="font-size: 12px;" v-if="errorOtp && !disabled")
                      | Запросить
                      span(class="mx-1 text-lowercase") код
                      span(class="text-lowercase") повторно
                    div(v-if="disabled" class="font-weight-bold text-center mb-6") Запросить код можно будет через 20 секунд
                v-window-item(:value="3 && !complete")
                  div(class="font-weight-bold pl-4 text-left") Новый пароль
                  v-text-field(
                    solo 
                    label="Пароль"
                    @input="changeInput"
                    class="input"
                    v-model="password"
                    :rules="passwordRules" 
                  )
                v-btn(
                  :disabled="!valid" 
                  class="text-capitalize white--text font-weight-bold" 
                  rounded 
                  v-if="!complete"
                  @click="nextStep(stage)"
                  color="costumBlue"
                ) Далее
</template>

<script>
import axios from "axios";

export default {
  name: "RestorePassword",
  data: () => ({
    valid: false,
    email: null,
    errorEmail: null,
    code: null,
    loading: false,
    disabled: false,
    errorOtp: null,
    validCode: null,
    complete: false,
    emailRules: [
      (v) => !!v || "Email обязателен",
      (v) => /.+@.+\..+/.test(v) || "Не корректный email",
    ],
    passwordRules: [(v) => !!v || "Пароль обязателен"],
    password: null,
    steps: [
      {
        id: 1,
        name: "Почта",
        title: true,
        number: "01",
        active: true,
        complete: false,
      },
      {
        id: 2,
        name: "Код",
        title: true,
        number: "02",
        active: false,
        complete: false,
      },
      {
        id: 3,
        name: "Пароль",
        title: true,
        number: "03",
        active: false,
        complete: false,
      },
    ],
    user_id: null,
    stage: 1,
    steps_index: 0,
  }),
  methods: {
    changeInput() {
      this.errorEmail = null;
      this.errorOtp = null;
    },
    nextStep(stage) {
      if (stage === 1) {
        // Проверяем email
        axios
          .get(this.$store.state.api_url + "check_email/", {
            params: {
              email: this.email,
            },
          })
          .then((response) => {
            if (response.data.status) {
              // Получаем id пользователя для дальнейшего измененния его пароля
              this.user_id = response.data.user[0].id;

              this.steps[0].active = false;
              this.steps[0].complete = true;
              this.stage = 2;
              this.steps[1].active = true;
              this.valid = false;
              this.getCode();
            } else {
              this.valid = false;
              this.errorEmail = "Такого email не существует";
            }
          });
      } else if (this.stage === 2) {
        this.loading = true;
        setTimeout(() => {
          this.loading = false;
          if (this.code === this.validCode) {
            this.steps[1].active = false;
            this.steps[1].complete = true;
            this.stage = 3;
            this.steps[2].active = true;
            this.valid = false;
          } else {
            this.valid = false;
            this.errorOtp = "Код не верный";
          }
        }, 3500);
      } else if (this.stage === 3) {
        // Получаем данные пользователя
        axios
          .get(this.$store.state.api_url + `users/${this.user_id}/`)
          .then((response) => {
            const user = response.data;
            console.log(user);

            const formData = new FormData();

            // FormData
            formData.append("first_name", user.first_name);
            formData.append("last_name", user.last_name);
            formData.append("username", user.username);
            formData.append("password", this.password);
            formData.append("telegram_username", user.telegram_username);
            formData.append("phone", user.phone);
            formData.append("is_active", true);

            axios
              .put(
                this.$store.state.api_url + `users/${this.user_id}/`,
                formData
              )
              .then(() => {
                this.complete = true;

                setTimeout(() => {
                  this.$router.push("/signin");
                }, 2000);
              });
          });
      }
    },
    getCode() {
      // Получаем код по API для валидации
      // Также отправляется письмо на почту
      axios
        .post(this.$store.state.api_url + "reset_password/", {
          email: this.email,
        })
        .then((response) => {
          console.log(response.data);
          this.validCode = response.data;
        });
    },
    repeatCode() {
      this.code = null;
      this.errorOtp = null;
      this.getCode();

      this.disabled = true;
      setTimeout(() => {
        this.disabled = false;
      }, 20000);
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
}

h1 {
  font-size: 30px;
  line-height: initial;
}

.left-complete {
  & > *:first-child {
    margin-bottom: 76px;
    font-size: 82px !important;
  }
}

.step {
  &-title {
    font-weight: 600;
    font-size: 28px;
    line-height: 33px;
    letter-spacing: 0.02em;
    color: #afafaf;
  }
  &-step {
    align-items: center;
    font-weight: 500;
    font-size: 18px;
    display: flex;
    flex-direction: column;
    line-height: 21px;
    text-align: center;
    gap: 6px;
    color: #959595;

    & > div {
      width: 50px;
      height: 50px;
      justify-content: center;
      display: flex;
      font-size: 24px;
      padding-right: 2px;
      font-size: 20px;
      align-items: center;
      background: linear-gradient(180deg, #dcdcdc 0%, #ebebeb 100%);
      border-radius: 50%;
      letter-spacing: 0.02em;
      color: #959595;
    }
  }

  &-ul {
    list-style: none !important;
    gap: 50px;
    justify-content: center;
  }
}

.active {
  & > div {
    background: linear-gradient(180deg, #ff5722 0%, #ff7043 100%) !important;
    color: #ffffff !important;
  }

  color: #212121 !important;
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}
</style>
