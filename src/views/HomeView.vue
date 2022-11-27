<template lang="pug">
div
  header
    home-header
  main
    about-home
    about-services-home
  footer
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeHeader from "@/components/HomeHeader";
import AboutServicesHome from "@/components/AboutServicesHome";
import AboutHome from "@/components/AboutHome";

export default {
  name: "HomeView",
  data() {
    return {};
  },
  components: { HomeHeader, AboutServicesHome, AboutHome },
  mixins: [updateTitle],
  created() {
    this.updateTitle(this.$t("main"));
  },
};
</script>

<style scoped lang="scss"></style>
