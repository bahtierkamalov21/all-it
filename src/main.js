import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import i18n from "./plugins/i18n";
import vuetify from "./plugins/vuetify";
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
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

library.add(
  faEarthAsia,
  faLaptopCode,
  faCloud,
  faGlobe,
  faArrowUp,
  faCircleCheck,
  faPlus
);

Vue.component("font-awesome-icon", FontAwesomeIcon);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
