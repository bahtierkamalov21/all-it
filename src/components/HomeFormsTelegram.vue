<template lang="pug">
div
  v-col 
    v-row(class="container ma-0")
      div(class="left rounded-xl pa-12")
        div(class="font-weight-bold text-center text-uppercase mb-6")
          | Отправте заявку в Telegram
          br
          | наш консультант свяжется с вами
        v-form(class="text-center" ref="form" v-model="valid" lazy-validation @submit.prevent="submitForm")
          v-text-field(
            v-model="username"
            :rules="[v => !!v || '']"
            required
            hide-details
            solo
            class="mb-4"
            label="Telegram username" 
            class="input"
            prepend-inner-icon="mdi-account"
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
    };
  },
  methods: {
    submitForm() {
      if (this.$refs.form.validate()) {
        this.message = `<b>Telegram username отправителя: ${this.username}</b>\n`;
        this.message += `<b>Номер телефона отправителя: ${this.phone}</b>\n`;
        this.message += `<b>Заказчик: ${this.radios}</b>\n`;
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
  box-shadow: var(--shadow-2xl);
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

input {
  border: 1px solid #fff;
  height: 48px;
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
