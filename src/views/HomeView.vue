<template lang="pug">
div
  header
    home-header
  main
    about-services-home
  footer
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeHeader from "@/components/HomeHeader";
import AboutServicesHome from "@/components/AboutServicesHome";

export default {
  name: "HomeView",
  data() {
    return {};
  },
  components: { HomeHeader, AboutServicesHome },
  mixins: [updateTitle],
  created() {
    this.updateTitle(this.$t("main"));
  },
};
</script>

<style scoped lang="scss"></style>
