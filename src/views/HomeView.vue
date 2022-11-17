<template lang="pug">
div
  div(class="header")
    v-container
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import LeftDrawerView from "@/components/LeftDrawerView";

export default {
  name: "HomeView",
  data() {
    return {};
  },
  mixins: [updateTitle],
  components: { LeftDrawerView },
  created() {
    this.updateTitle(this.$t("main"));
  },
};
</script>

<style scoped lang="scss">
.header {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--v-background-base);
  min-height: calc(100vh - 56px);

  &-wrapper {
    border-radius: 16px !important;
    box-shadow: 0 5px 15px rgb(0 0 0 / 15%) !important;
    background-color: #fff;
    min-height: calc(75vh);
    padding: 25px;

    & > h1 {
      background: -webkit-linear-gradient(45deg, #09009f, #00ff95 80%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  }
}
</style>
