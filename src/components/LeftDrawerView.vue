<template lang="pug">
div
  div(class="drawer" :style="heightDrawer")
    div(class="drawer-content")
      | aasdas
</template>

<script>
export default {
  name: "LeftDrawerView",
  data() {
    return {
      drawer: true,
      arrayHeightDrawer: [
        {
          height: "calc(100vh - 56px)",
        },
        {
          height: "calc(100vh - 106px)",
        },
      ],
      heightDrawer: null,
    };
  },
  methods: {
    selectPlusHeight() {
      this.$store.state.hideWarning
        ? (this.heightDrawer = this.arrayHeightDrawer[0])
        : (this.heightDrawer = this.arrayHeightDrawer[1]);
    },
  },
  created() {
    this.selectPlusHeight();
  },
};
</script>

<style scoped lang="scss">
.drawer {
  width: 68px;
  backdrop-filter: 16px;
  display: flex;
  justify-content: right;
  align-items: center;

  &-content {
    background-color: #fff;
    width: 56px;
    border-radius: 5px;
    box-shadow: 0 5px 15px rgb(0 0 0 / 15%);
    height: 80%;
  }
}
</style>
