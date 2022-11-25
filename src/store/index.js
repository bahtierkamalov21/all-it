import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    theme: null,
  },
  getters: {},
  mutations: {
    changeTheme(state, payload) {
      state.theme = payload;
    },
  },
  actions: {},
  modules: {},
});
