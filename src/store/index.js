import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    theme: null,
    user: null,
    api_url: "http://localhost:8000/api/v1/",
    token: "5944619606:AAEgXlAvmwjvWcH84eMlLdPL7RX4BTTqcEM",
    chat_id: "-1001849968025",
  },
  getters: {},
  mutations: {
    changeTheme(state, payload) {
      state.theme = payload;
    },
    setUser(state, payload) {
      state.user = payload;
    },
  },
  actions: {},
  modules: {},
});
