import Vue from "vue";
import VueI18n from "vue-i18n";
import ruLanguage from "../languages/ru.json";
import enLanguage from "../languages/en.json";

Vue.use(VueI18n);

export default new VueI18n({
  locale: "en",
  messages: {
    ruLanguage,
    enLanguage,
  },
});
