<template lang="pug">
div
  div(class="bottom-sheet" :class="{'active' : open}")
    v-card(class="card pa-4")
      v-col
        v-row(class="justify-spase-between")
          div Меню
          v-btn(icon)
      | ascasc
</template>

<script>
export default {
  name: "TopSheetMenu",
  watch: {
    open() {
      this.setOpen();
    },
  },
  props: {
    open: Boolean,
  },
  mounted() {
    window.addEventListener("click", (event) => {
      if (event.target === document.querySelector(".bottom-sheet")) {
        this.$emit("setOpen", !this.open);
      } else null;
    });
  },
  methods: {
    setOpen() {
      this.$emit("setOpen", this.open);
    },
  },
};
</script>

<style scoped lang="scss">
.bottom-sheet {
  position: fixed;
  width: 100vw;
  height: 100vh;
  z-index: 120;
  left: 0;
  top: 0;
  overflow: hidden;
  display: none;

  & .active > .card {
    transition: 2s ease-in-out;
    transform: translateY(0);
  }
}

.active {
  display: block;
}

.card {
  border-radius: 0 0 10px 10px;
  transform: translateY(-100%);
  transition: 2s ease-in-out;
}
</style>
