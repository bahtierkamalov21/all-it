<template lang="pug">
div
  header(class="header pb-12")
    v-container(v-if="user")
      v-col
        v-row(class="ma-0" style="gap: 12px;")
          div(class="left")
            v-card(class="card pa-6 rounded-xl" elevation="0")
              v-chip(class="white--text pr-6" color="costumBlue")
                v-icon mdi-information-variant
                | Изменения данных вступят в силу после рассмотрения администрацией
              div(class="d-flex my-6" style="gap: 12px;")
                div(class="text-center avatar-container rounded-lg pa-6")
                  div(class="avatar ma-auto")
                    v-img(:src="user.avatar" v-if="user.avatar")
                    v-icon(v-else) mdi-account-circle
                  div(class="username rounded-lg pa-2 px-4 white--text mt-4") {{ user.first_name }} {{ user.last_name }}
                div(style="width: 100%;")
                  v-text-field(v-model="user.first_name" rounded label="Имя" hide-details @input="changeUserData")
                  v-text-field(v-model="user.last_name" rounded label="Фамилия" hide-details @input="changeUserData")
                  v-text-field(v-model="user.username" rounded label="Username" hide-details @input="changeUserData")
                  v-text-field(v-model="user.telegram_username" rounded label="Telegram username" hide-details @input="changeUserData")
                  v-text-field(v-model="user.email" rounded label="Email" hide-details @input="changeUserData")
                  v-text-field(v-model="user.phone" rounded label="Номер телефона" hide-details @input="changeUserData")
              div(class="d-flex justify-space-between")
                v-btn(@click="exitSystem" class="delete pa-0" color="red" min-width="38" rounded elevation="0")
                  v-icon(color="white") mdi-delete
                  div(class="delete-text font-weight-bold") Выйти из системы
                v-btn(:disabled="!update" @click="sendMessageInTelegramAbouUpdateUserData" color="costumBlue" rounded class="white--text text-capitalize" elevation="0")
                  | Сохранить
                  span(class="text-lowercase ml-1") изменения
          div(class="right")
            v-card(class="card pa-6 rounded-xl" elevation="0")
              v-card-subtitle Мои заявки на проекты
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileView",
  data() {
    return {
      user: null,
      user_copied: null,
      update: false,
      message: null,
    };
  },
  created() {
    this.determineWhetherUserAuthorized();
    this.getUserData();
  },
  methods: {
    // Determine whether the user is authorized
    determineWhetherUserAuthorized() {
      if (!this.$store.state.user) {
        this.$router.push("/signin");
      } else null;
    },
    changeUserData() {
      this.update = true;
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
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
    sendMessageInTelegramAbouUpdateUserData() {
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

.left {
  flex-grow: 1;
}

.right {
  flex-grow: 2;
}

.card {
  box-shadow: var(--shadow-2xl) !important;
  overflow: hidden;
}

.username {
  background-color: var(--custom-blue);
  max-width: 164px;
  min-width: 164px;
  transition: all 0.2s ease-in-out;
}

.avatar {
  height: 150px;
  width: 150px;
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

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}
</style>
