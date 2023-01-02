<template lang="pug">
div
  v-col 
    v-row 
      div(class="left rounded-xl pa-12")
        div(class="font-weight-bold text-center text-uppercase mb-6")
          | Отправте заявку нам в телеграм
          br
          | наш консультант свяжется с вами
        v-form(class="text-center" ref="form" v-model="valid" lazy-validation @submit.prevent="submitForm")
          v-text-field(
            v-model="username"
            outlined
            :rules="[v => !!v || '']"
            required
            hide-details
            class="mb-4"
            label="Telegram username" 
            prepend-inner-icon="mdi-account"
          )
          v-text-field(
            :rules="phoneRules"
            outlined
            v-model="phone"
            required
            label="Номер телефона" 
            prepend-inner-icon="mdi-phone"
            hide-details
          )
          v-radio-group(v-model="radios" hide-details required :rules="[v => !!v || '']") 
            v-radio(label="Физическое лицо" value="Физическое лицо")
            v-radio(label="Компания" value="Компания")
          v-checkbox(v-model="agree" required :rules="[v => !!v || 'Вы должны согласиться с политикой конфиденциальности']")
            template(v-slot:label)
              v-card(elevation="0" class="agree pa-2 px-4")
                div принимаю 
                router-link(to="/" class="d-flex text-decoration-none") политику конфиденциальности
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
  width: 50%;
  max-width: 460px;
}

.right {
  width: 50%;
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

@media screen and (max-width: 1086px) {
  .left {
    width: 70%;
  }

  .right {
    width: 30%;
  }
}
</style>
