import store from "../store";
import router from "../router";

export default {
  methods: {
    exitSystem(reload) {
      // Очистка localStorage
      localStorage.clear();
      // Очистка store
      store.commit("setUser", null);
      store.commit("setDecoded", null);
      store.commit("setTokenAccess", null);
      store.commit("setTokenRefresh", null);
      store.commit("setUsername", null);
      store.commit("setPassword", null);
      // Push in home page
      reload ? location.reload() : router.push("/");
    },
  },
};
