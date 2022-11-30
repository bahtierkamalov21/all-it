<template lang="pug">
div
  header
    home-header
  main
    about-home
    home-services
    home-projects
  footer
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeHeader from "@/components/HomeHeader";
import AboutHome from "@/components/AboutHome";
import HomeServices from "@/components/HomeServices";
import HomeProjects from "@/components/HomeProjects";

export default {
  name: "HomeView",
  data() {
    return {};
  },
  components: { HomeProjects, HomeHeader, AboutHome, HomeServices },
  mixins: [updateTitle],
  created() {
    this.updateTitle(this.$t("main"));
  },
};
</script>

<style scoped lang="scss"></style>
