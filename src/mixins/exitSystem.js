export default {
  methods: {
    exitSystem(reload) {
      // Очистка localStorage
      localStorage.clear();
      // Очистка store
      this.$store.commit("setUser", null);
      this.$store.commit("setDecoded", null);
      this.$store.commit("setTokenAccess", null);
      this.$store.commit("setTokenRefresh", null);
      this.$store.commit("setUsername", null);
      this.$store.commit("setPassword", null);
      // Push in home page
      reload ? location.reload() : this.$router.push("/");
    },
  },
};
