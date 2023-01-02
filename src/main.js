import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import i18n from "./plugins/i18n";
import vuetify from "./plugins/vuetify";
import flag from "./plugins/flag";

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

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  vuetify,
  flag,
  render: (h) => h(App),
}).$mount("#app");
