import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    theme: null,
    user: null,
    api_url: "http://localhost:8000/api/v1/",
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
