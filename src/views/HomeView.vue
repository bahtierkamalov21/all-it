<template lang="pug">
div
  div(class="header")
    left-drawer-view
    v-container
      v-card(class="header-wrapper")
        h1 IT Разработка
        h2 Соверменных
          br
          | Проектов
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
  background: linear-gradient(90deg, #effaff 0%, #d9e7ff 100%);

  &-wrapper {
    border-radius: 16px !important;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.05) !important;
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
