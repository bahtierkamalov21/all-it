import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import i18n from "./plugins/i18n";
import vuetify from "./plugins/vuetify";
import flag from "./plugins/flag";
import axios from "axios";

// FontAwesomeIcons
import { library } from "@fortawesome/fontawesome-svg-core";

import {
  faEarthAsia,
  faLaptopCode,
  faCloud,
  faGlobe,
  faArrowUp,
  faCircleCheck,
  faPlus,
  faBars,
  faHouse,
  faLayerGroup,
} from "@fortawesome/free-solid-svg-icons";

import { faTelegram, faGoogle } from "@fortawesome/free-brands-svg-icons";

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(
  faEarthAsia,
  faLaptopCode,
  faCloud,
  faGlobe,
  faArrowUp,
  faCircleCheck,
  faPlus,
  faBars,
  faTelegram,
  faHouse,
  faGoogle,
  faLayerGroup
);

import exitSystem from "./mixins/exitSystem";

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

// Получение данных пользователя
function getUserData() {
  if (localStorage.getItem("user")) {
    const decoded = JSON.parse(localStorage.getItem("decoded"));

    axios
      .get(store.state.api_url + `users/${decoded.user_id}/`)
      .then((response) => {
        // Сохраняем данные пользователя в store и localStorage
        localStorage.setItem("user", JSON.stringify(response.data));
        store.commit("setUser", JSON.stringify(response.data));
      })
      .catch(() => {
        // Ошибка возможна если пользователя нет в БД
        exitSystem.methods.exitSystem({ reload: true });
      });
  } else null;
}

getUserData();

new Vue({
  router,
  store,
  i18n,
  vuetify,
  flag,
  render: (h) => h(App),
}).$mount("#app");
