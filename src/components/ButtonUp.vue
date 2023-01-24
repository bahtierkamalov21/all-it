<template lang="pug">
div
  transition(name="fade")
    v-card(@click="toUp" width="52" height="52" class="button d-flex justify-center align-center" v-if="active")
      font-awesome-icon(icon="fa-solid fa-arrow-up")
</template>

<script>
export default {
  name: "ButtonUp",
  data() {
    return {
      active: false,
    };
  },
  methods: {
    toUp() {
      window.scrollTo(0, 0);
    },
  },
  mounted() {
    window.addEventListener("scroll", () => {
      window.scrollY >= 450 ? (this.active = true) : (this.active = false);
    });
  },
};
</script>

<style scoped lang="scss">
.button {
  position: fixed;
  right: 25px;
  bottom: 25px;
  overflow: hidden;
  border-radius: 50% !important;
  box-shadow: 0 0 12px 0 rgb(0 0 0 / 50%) !important;
  z-index: 5;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active до версии 2.1.8 */ {
  opacity: 0;
}

@media screen and (max-width: 1086px) {
  .button {
    right: 25px;
    bottom: 75px;
  }
}
</style>
