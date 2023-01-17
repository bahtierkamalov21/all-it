<template lang="pug">
div
  dialog-reviews(
    :dialogReviews="dialogReviews" 
    @getDialogReviews="getDialogReviews" 
    @getHaveReviews="getHaveReviews"
  )
  dialog-projects(
    :dialogProjects="dialogProjects" 
    @getDialogProjects="getDialogProjects"
  )
  header(class="header pb-12")
    loading-item(v-if="!user")
    v-container(v-else)
      v-card(class="card rounded-xl ma-auto" max-width="960")
        div(class="d-flex justify-center mb-6 pl-6 pr-12")
          div(class="ml-auto avatar" @click="callChangeAvatar")
            v-img(width="100%" height="100%" :src="user.avatar" v-if="user.avatar")
            v-icon(v-else color="#707070") mdi-account-circle
          input(
            style="display: none;" 
            ref="inputAvatar" 
            type="file" 
            accept="image/jpeg, image/png, image/svg, image/jpg" 
            @change="changeAvatar()"
          )
          div(class="ml-auto")
            v-img(src="@/assets/icons/settings-profile.svg")
        v-card(class="d-flex align-start ma-auto px-4" style="margin-top: 86px !important;" elevation="0" max-width="820")
          v-chip(class="white--text pr-6" color="costumBlue")
            v-icon mdi-information-variant
            | Изменения данных вступят в силу после рассмотрения администрацией
        v-card(class="userdata d-flex align-start ma-auto px-6 mt-6" elevation="0" max-width="720")
          v-form(ref="form" v-model="valid" lazy-validation @submit.prevent="sendMessageInTelegramAbouUpdateUserData")
            div
              v-card-text(class="pa-0") Имя
              v-text-field(v-model="user.first_name" class="input" solo label="Имя" @input="changeUserData")
              v-card-text(class="pa-0") Фамилия
              v-text-field(v-model="user.last_name" class="input" solo label="Фамилия" @input="changeUserData")
              v-card-text(class="pa-0") Username
              v-text-field(
                v-model="user.username" 
                :rules="[v => !!v || 'Имя пользователя обязательно']" 
                class="input" 
                solo 
                rounded 
                label="Username" 
                @input="changeUserData"
              )
            div
              v-card-text(class="pa-0") Telegram username
              v-text-field(
                v-model="user.telegram_username" 
                :rules="telegramUsernameRules" 
                class="input" 
                solo 
                label="Telegram username" 
                @input="changeUserData"
              )
              v-card-text(class="pa-0") Email
              v-text-field(v-model="user.email" class="input" solo label="Email" @input="changeUserData")
              v-card-text(class="pa-0") Телефон
              v-text-field(
                v-model="user.phone" 
                :rules="phoneRules" 
                class="input" 
                solo 
                label="Номер телефона" 
                @input="changeUserData"
              )
        div(class="text-center pb-6")
          v-btn(
            :disabled="!update && !valid" 
            @click="sendMessageInTelegramAbouUpdateUserData" 
            color="costumBlue" 
            rounded 
            class="white--text text-capitalize" 
            elevation="0"
          )
            | Отправить
            span(class="text-lowercase ml-1") изменения
          v-btn(@click="exitSystem" class="delete pa-0 ml-6 mt-4" color="red" min-width="38" rounded elevation="0")
            v-icon(color="white") mdi-delete
            div(class="delete-text font-weight-bold") Выйти из системы
      div(class="prompts d-flex flex-wrap justify-space-between ma-auto my-6" style="max-width: 960px;")
        div(class="text-left mb-6")
          v-btn( 
            v-if="!haveReviews"
            @click="dialogReviews = !dialogReviews"
            color="costumBlue" 
            rounded 
            class="white--text text-capitalize" 
            elevation="0"
          )
            v-icon(left) mdi-typewriter
            | Оставить
            span(class="text-lowercase ml-1") отзыв
          v-chip(class="d-block mt-2 pr-6")
            v-icon mdi-information-variant
            | Можно оставить только один отзыв
        div(class="text-right")  
          v-btn( 
            @click="dialogProjects = !dialogProjects"
            color="costumBlue" 
            rounded 
            class="white--text text-capitalize" 
            elevation="0"
          )
            v-icon(left) mdi-file-document-edit
            | Заполнить
            span(class="text-lowercase ml-1") анкету своего проекта
          v-chip(class="d-block mt-2 pr-6")
            v-icon mdi-information-variant
            | Можно заполнить после завершения текущего проекта
</template>

<script>
import axios from "axios";
import LoadingItem from "@/components/LoadingItem";
import DialogReviews from "@/components/DialogReviews";
import DialogProjects from "@/components/DialogProjects";

export default {
  name: "ProfileView",
  data() {
    return {
      user: null,
      user_copied: null,
      haveReviews: null,
      update: false,
      message: null,
      valid: false,
      avatar: null,
      phone_regex: /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/,
      phoneRules: [
        (v) => this.phone_regex.test(v) || "Неверно введен номер телефона",
      ],
      telegram_username_regex: /^@[A-Za-z\d_]{5,32}$/,
      telegramUsernameRules: [
        (v) =>
          this.telegram_username_regex.test(v) ||
          "Неверно введен telegram username",
      ],
      dialogReviews: false,
      dialogProjects: false,
    };
  },
  components: { LoadingItem, DialogReviews, DialogProjects },
  created() {
    this.determineWhetherUserAuthorized();
  },
  methods: {
    getHaveReviews(data) {
      this.haveReviews = data;
    },
    getDialogReviews(data) {
      this.dialogReviews = data;
    },
    getDialogProjects(data) {
      this.dialogProjects = data;
    },
    // Determine whether the user is authorized
    determineWhetherUserAuthorized() {
      !localStorage.getItem("user")
        ? this.$router.push("/signin")
        : this.getUserData();
    },
    changeUserData() {
      this.update = true;
    },
    callChangeAvatar() {
      this.$refs.inputAvatar.click();
    },
    changeAvatar() {
      const file = this.$refs.inputAvatar.files[0];
      const formData = new FormData();
      formData.append("avatar", file);
      formData.append("username", this.user.username);
      formData.append("password", this.user.password);
      formData.append("telegram_username", this.user.telegram_username);
      const decoded = JSON.parse(localStorage.getItem("decoded"));
      axios
        .put(this.$store.state.api_url + `users/${decoded.user_id}/`, formData)
        .then(() => {
          this.getUserData();
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
    exitSystem() {
      // Очистка localStorage
      localStorage.clear();
      // Очистка store
      this.$store.commit("setUser", null);
      this.$store.commit("setDecoded", null);
      this.$store.commit("setTokenAccess", null);
      this.$store.commit("setTokenRefresh", null);
      // Push in home page
      this.$router.push("/");
    },
    getUserData() {
      const decoded = JSON.parse(localStorage.getItem("decoded"));
      axios
        .get(this.$store.state.api_url + `users/${decoded.user_id}/`)
        .then((response) => {
          // Сохраняем данные пользователя в store и localStorage
          localStorage.setItem("user", JSON.stringify(response.data));
          this.$store.commit("setUser", JSON.stringify(response.data));

          this.user = response.data;
          this.user_copied = response.data;

          // Сохранение отзыва пользователя
          this.haveReviews = response.data.review;
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
    sendMessageInTelegramAbouUpdateUserData() {
      if (this.$refs.form.validate()) {
        let listData = {};
        // Проверка входных данных
        for (const key in this.user) {
          if (this.user[key] !== this.user_copied[key]) {
            listData[key] = this.user[key];
          }
        }
        // Отправка сообщения в телеграмм
        this.message = `<b>Telegram username отправителя: ${this.user_copied.username}</b>\n`;
        this.message += `<b>API id пользователя: ${this.user.id}</b>\n`;
        this.message += `<b>Требует смену данных профиля на: </b>\n`;
        this.message += `<b>${JSON.stringify(listData)}</b>`;
        const api_url = `https://api.telegram.org/bot${this.$store.state.token}/sendMessage`;
        axios
          .post(api_url, {
            chat_id: this.$store.state.chat_id,
            parse_mode: "html",
            text: this.message,
          })
          .then(() => {})
          .catch((errors) => {
            console.log(errors);
          });
      } else this.update = false;
    },
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style scoped lang="scss">
.header {
  min-height: 50vh;
  padding-top: 126px;
}

.card {
  box-shadow: var(--shadow-2xl) !important;
  overflow: hidden;

  & > *:first-child {
    position: relative;
    background: rgba(98, 197, 102, 0.5);

    & > *:last-child {
      width: 150px;
      height: 100px;
    }
  }
}

.child-card {
  box-shadow: var(--shadow-2xl) !important;
}

.userdata {
  gap: 24px;

  & > * {
    width: 100%;
  }
}

.username {
  background-color: var(--custom-blue);
  max-width: 164px;
  min-width: 164px;
  transition: all 0.2s ease-in-out;
}

.avatar {
  margin-right: 25%;
  position: absolute;
  top: 40px;
  height: 130px;
  width: 130px;
  border-radius: 50%;
  background-color: #f5f5f5;
  border: 2px solid #999;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  cursor: pointer;

  &-container {
    background-image: url("../assets/images/card-two-background.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    box-shadow: var(--shadow-2xl);
  }

  & > *:last-child {
    font-size: 165px;
  }
}

.delete {
  display: block;
  position: relative;

  &-text {
    position: absolute;
    right: -192px;
  }
}

@media screen and (max-width: 860px) {
  .prompts {
    & > *:last-child {
      width: 100%;

      & > *:last-child {
        width: max-content;
        margin-left: auto;
      }
    }
  }
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}

@media screen and (max-width: 600px) {
  .userdata {
    display: block !important;
  }
  .avatar {
    margin-right: 45%;
  }
}
</style>
