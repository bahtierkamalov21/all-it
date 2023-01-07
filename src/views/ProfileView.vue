<template lang="pug">
div
  header(class="header pb-12")
    v-container(v-if="user")
      v-col
        v-row(class="ma-0" style="gap: 12px;")
          div(class="left")
            v-card(class="card pa-6 rounded-xl" elevation="0")
              v-chip(class="pr-6")
                v-icon mdi-information-variant
                | Изменения данных вступят в силу после рассмотрения администрацией
              div(class="d-flex my-6" style="gap: 12px;")
                div(class="text-center")
                  div(class="avatar")
                    v-img(:src="user.avatar" v-if="user.avatar")
                    v-icon(v-else) mdi-account-circle
                  v-chip(class="white--text mt-2" color="costumBlue") {{ user.first_name }} {{ user.last_name }}
                div
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
      this.$store.commit("setTokenAccess", null);
      this.$store.commit("setTokenRefresh", null);
      // Push in home page
      this.$router.push("/");
    },
    getUserData() {
      // Преобразуем JSON в объект
      this.user = JSON.parse(this.$store.state.user);
      this.user_copied = JSON.parse(this.$store.state.user);
    },
    sendMessageInTelegramAbouUpdateUserData() {
      let listData = {};
      // Проверка входных данных
      if (this.user_copied.username !== this.user.username) {
        listData.username = this.user.username;
      }
      if (this.user_copied.first_name !== this.user.first_name) {
        listData.first_name = this.user.first_name;
      }
      if (this.user_copied.last_name !== this.user.last_name) {
        listData.last_name = this.user.last_name;
      }
      if (this.user_copied.telegram_username !== this.user.telegram_username) {
        listData.telegram_user = this.user.telegram_user;
      }
      if (this.user_copied.email !== this.user.email) {
        listData.email = this.user.email;
      }
      if (this.user_copied.phone !== this.user.phone) {
        listData.phone = this.user.phone;
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
