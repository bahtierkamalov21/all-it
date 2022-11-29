<template lang="pug">
div
  v-bottom-sheet(v-model="open")
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
  methods: {
    setOpen() {
      this.$emit("setOpen", this.open);
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  border-radius: 0 0 10px 10px;
  position: fixed;
  top: 0;
}
</style>
