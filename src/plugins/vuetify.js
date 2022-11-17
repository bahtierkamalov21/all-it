import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: { customProperties: true },
    themes: {
      light: {
        primary: "#3f51b5",
        background: "#f5f5f5",
        secondary: "#b0bec5",
        accent: "#8c9eff",
        error: "#b71c1c",
        content: "#ffffff",
        custom_title: "#666666",
      },
      dark: {
        background: "#1c1c1c",
        content: "#000000",
        custom_title: "#ffffff",
      },
    },
  },
});