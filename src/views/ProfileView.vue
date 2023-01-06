<template lang="pug">
div
  header(class="header pb-12")
    v-container
      v-col
        v-row(class="ma-0" style="gap: 12px;")
          div(class="left")
            v-card(class="card pa-6 rounded-xl" elevation="0")
              div(class="d-flex")
                div(class="avatar")
                  v-img
              v-btn(@click="exitSystem" class="delete pa-0" color="red" min-width="38" rounded elevation="0")
                v-icon(color="white") mdi-delete
                div(class="delete-text font-weight-bold") Выйти из системы
          div(class="right")
            v-card(class="card pa-6 rounded-xl" elevation="0")
              | ascas
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
      // Очистка localStorage
      localStorage.clear();
      // Очистка store
      this.$store.commit("setUser", null);
      this.$store.commit("setTokenAccess", null);
      this.$store.commit("setTokenRefresh", null);
      this.$router.push("/");
    },
  },
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>

<style scoped lang="scss">
.header {
  min-height: 50vh;
  padding-top: 126px;
}

.left {
  flex-grow: 1;
}

.right {
  flex-grow: 2;
}

.card {
  box-shadow: var(--shadow-2xl) !important;
}

.delete {
  position: relative;

  &-text {
    position: absolute;
    right: -190px;
  }
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}
</style>
