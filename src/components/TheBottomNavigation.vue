<template lang="pug">
div
  v-bottom-navigation(
    fixed
    shift
    class="navigation"
    v-model="value"
    grow
  )
    v-btn(v-for="item in buttons" :key="item.id" @click="pushLocation(item.link)")
      span {{ item.span }}
      v-icon mdi-{{ item.icon }}
    v-btn(@click="pushSupport")
      span Support
      v-icon mdi-lifebuoy
    v-btn(@click="pushLocation('/profile')")
      span Profile
      v-icon mdi-{{ profileIcon }}
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "TheBottomNavigation",
  data() {
    return {
      value: null,
      profileIcon: null,
      buttons: [
        {
          span: "Home",
          icon: "home",
          link: "/",
        },
        {
          span: "Projects",
          icon: "semantic-web",
          link: "/projects",
        },
      ],
    };
  },
  created() {
    // Get profile in localStorage
    this.changeProfileIcon();
    switch (this.$route.path) {
      case "/":
        this.value = 0;
        break;
      case "/projects":
        this.value = 1;
        break;
      case "/profile":
        this.value = 3;
        break;
      case "/signin":
        this.value = 3;
        break;
      case "/signup":
        this.value = 3;
        break;
    }
  },
  watch: {
    user() {
      this.changeProfileIcon();
    },
  },
  methods: {
    pushSupport() {
      window.scrollTo(0, document.body.scrollHeight);
    },
    changeProfileIcon() {
      this.profileIcon = this.user ? "account-check" : "account-circle";
    },
    pushLocation(path) {
      window.scrollTo(0, 0);
      if (path !== this.$route.path) {
        this.$router.push(path);
      } else null;
    },
  },
  computed: {
    ...mapState(["user"]),
  },
};
</script>

<style scoped lang="scss">
.navigation {
  z-index: 120;
  display: none;
}

@media screen and (max-width: 1142px) {
  .navigation {
    display: flex;
  }
}
</style>
