import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    user: null,
    token_access: null,
    token_refresh: null,
    api_url: "http://localhost:8000/api/v1/",
    // api_url: "https://localhost:8200/api/v1/",
    // api_url: "http://213.189.216.118:8200/api/v1/",
    // api_url: "http://213.189.216.118/api/v1/",
    token: "5944619606:AAEgXlAvmwjvWcH84eMlLdPL7RX4BTTqcEM",
    chat_id: "-1001849968025",
    decoded: null,
    username: null,
    password: null,
    myProjects: null,
  },
  getters: {},
  mutations: {
    setUser(state, payload) {
      state.user = payload;
    },
    setTokenAccess(state, payload) {
      state.token_access = payload;
    },
    setTokenRefresh(state, payload) {
      state.token_refresh = payload;
    },
    setDecoded(state, payload) {
      state.decoded = payload;
    },
    setUsername(state, payload) {
      state.username = payload;
    },
    setPassword(state, payload) {
      state.password = payload;
    },
    setMyProjects(state, payload) {
      state.myProjects = payload;
    },
  },
  actions: {},
  modules: {},
});
