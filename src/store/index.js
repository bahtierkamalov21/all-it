import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    theme: null,
    user: null,
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
