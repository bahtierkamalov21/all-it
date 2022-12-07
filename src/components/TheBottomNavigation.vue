<template lang="pug">
div
  v-bottom-navigation(
    fixed
    shift
    class="navigation"
    v-model="value"
    :background-color="color"
    grow
  )
    v-btn(v-for="item in buttons" :key="item.id" @click="pushLocation(item.link)")
      span {{ item.span }}
      v-icon mdi-{{ item.icon }}
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
        {
          span: "Support",
          icon: "lifebuoy",
          link: "/support",
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
    changeProfileIcon() {
      this.profileIcon = this.user ? "account-check" : "account-circle";
    },
    pushLocation(path) {
      if (path !== this.$route.path) {
        this.$router.push(path);
      } else null;
    },
  },
  computed: {
    ...mapState(["user"]),
    color() {
      switch (this.value) {
        case 0:
          return "#ffffff";
        default:
          return "#ffffff";
      }
    },
  },
};
</script>

<style scoped lang="scss">
.navigation {
  z-index: 120;
  display: none;
}

@media screen and (max-width: 900px) {
  .navigation {
    display: flex;
  }
}
</style>
