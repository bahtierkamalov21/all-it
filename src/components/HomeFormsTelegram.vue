<template lang="pug">
div
  v-col 
    v-row(class="container ma-0")
      div(class="left left-complete text-center rounded-xl pa-12" v-if="send")
        div(class="font-weight-bold text-center text-uppercase mb-6")
          | Спасибо за заявку
        v-icon(color="green") mdi-check-decagram
        v-card-text Ожидайте
          br
          | скоро оператор свяжется с вами 
      div(class="left rounded-xl pa-12" v-if="!send")
        div(class="font-weight-bold text-center text-uppercase mb-6")
          | Отправте заявку в Telegram
          br
          | наш консультант свяжется с вами
        v-form(class="text-center" ref="form" v-model="valid" lazy-validation @submit.prevent="submitForm")
          v-text-field(
            v-model="username"
            :rules="telegramUsernameRules"
            required
            hide-details
            solo
            class="mb-4"
            label="Telegram username" 
            class="input"
            prepend-inner-icon="mdi-account"
            type="text"
          )
          v-text-field(
            :rules="phoneRules"
            solo
            v-model="phone"
            required
            label="Номер телефона" 
            class="input"
            prepend-inner-icon="mdi-phone"
            hide-details
            type="tel"
          )
          v-radio-group(v-model="radios" hide-details required :rules="[v => !!v || '']") 
            v-radio(label="Физическое лицо" value="Физическое лицо")
            v-radio(label="Компания" value="Компания")
          v-btn(rounded elevation="0" min-height="52" @click="submitForm" class="white--text font-weight-bold px-16 mt-6" color="costumBlue")
            | Отправить
      div(class="right d-flex align-center justify-center")
        font-awesome-icon(
          icon="fa-brands fa-telegram"
          class="right-icon"
        )
</template>

<script>
import axios from "axios";

export default {
  name: "HomeFormsTelegram",
  data() {
    return {
      send: false,
      radios: null,
      agree: false,
      message: null,
      username: null,
      phone: null,
      valid: null,
      regex: /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/,
      phoneRules: [
        (v) => !!v || "Номер телефона обязателен",
        (v) => this.regex.test(v) || "Неверно введен номер телефона",
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
  methods: {
    submitForm() {
      if (this.$refs.form.validate()) {
        this.message = `<b>Заявка с сайта BMM LITER!!!</b>\n\n`;
        this.message += `<b>Telegram username: </b><i>${this.username}</i>\n`;
        this.message += `<b>Номер телефона отправителя: </b><i>${this.phone}</i>\n`;
        this.message += `<b>Заказчик: </b><i>${this.radios}</i>\n`;
        const api_url = `https://api.telegram.org/bot${this.$store.state.token}/sendMessage`;
        axios
          .post(api_url, {
            chat_id: this.$store.state.chat_id,
            parse_mode: "html",
            text: this.message,
          })
          .then(() => {
            this.message = null;
            this.phone = null;
            this.username = null;
            this.radios = null;
            this.send = true;
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
.left {
  box-shadow: var(--shadow-lg);
  max-width: 460px;
}

.right {
  flex-grow: inherit;
  position: relative;

  &-icon {
    font-size: calc(var(--section-title) * 3);
    color: var(--custom-blue);
  }
}

.agree {
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2) !important;

  & > *:first-child {
    color: rgba(0, 0, 0, 0.6);
  }
}

.left-complete {
  & > *:nth-child(2) {
    margin-top: 70px;
    margin-bottom: 76px;
    font-size: 82px !important;
  }
}

input {
  border: 1px solid #fff;
  height: 48px;
}

@media screen and (min-width: 1142px) {
  .right-icon {
    font-size: 10rem;
  }
}

@media screen and (max-width: 600px) {
  .container {
    flex-direction: column-reverse;
    gap: 24px;
    padding-left: 0;
  }

  .left {
    padding: 24px !important;
  }
}
</style>
