<template lang="pug">
div
  header
    home-header
  main
    about-home
    home-services
  footer
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeHeader from "@/components/HomeHeader";
import AboutHome from "@/components/AboutHome";
import HomeServices from "@/components/HomeServices";

export default {
  name: "HomeView",
  data() {
    return {};
  },
  components: { HomeHeader, AboutHome, HomeServices },
  mixins: [updateTitle],
  created() {
    this.updateTitle(this.$t("main"));
  },
};
</script>

<style scoped lang="scss"></style>
