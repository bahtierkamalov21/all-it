<template lang="pug">
div
  header(class="header")
    v-container
      v-col
        v-row(class="ma-0")
          div(class="left")
          div(class="right")
            v-btn(@click="exitSystem") Выйти из системы
</template>

<script>
export default {
  name: "ProfileView",
  created() {
    this.determineWhetherUserAuthorized();
  },
  methods: {
    // Determine whether the user is authorized
    determineWhetherUserAuthorized() {
      if (!this.$store.state.user) {
        this.$router.push("/signin");
      } else null;
    },
    exitSystem() {
      localStorage.clear();
      this.$store.commit("setUser", null);
      this.$store.commit("setTokenAccess", null);
      this.$store.commit("setTokenRefresh", null);
      this.$router.push("/");
    },
  },
};
</script>

<style scoped lang="scss">
.header {
  min-height: 50vh;
  padding-top: 126px;
}

.left {
  flex-grow: inherit;
}

.right {
  flex-grow: inherit;
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}
</style>
