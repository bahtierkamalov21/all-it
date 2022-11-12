<template lang="pug">
div
  div(class="drawer" :style="heightDrawer")
</template>

<script>
export default {
  name: "LeftDrawerView",
  data() {
    return {
      drawer: true,
      arrayHeightDrawer: [
        {
          height: "calc(100vh - 60px)",
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
  width: 56px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.05);
  background-color: #fff;
  backdrop-filter: 16px;
}
</style>
