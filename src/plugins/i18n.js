import Vue from "vue";
import VueI18n from "vue-i18n";
import ruLanguage from "../languages/ru.json";
import enLanguage from "../languages/en.json";

Vue.use(VueI18n);

var language;

function setLanguageDefault() {
  const systemLanguage = window.navigator.language.split("-")[0];
  if (systemLanguage === "ru" || systemLanguage === "en") {
    language = systemLanguage;
  } else language = "en";
}

setLanguageDefault();

export default new VueI18n({
  locale: language,
  messages: {
    ru: ruLanguage,
    en: enLanguage,
  },
});
