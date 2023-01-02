<template lang="pug">
div
  header
    home-header
  v-main
    about-home
    home-services
    home-reviews
    home-projects
    home-forms
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeHeader from "@/components/HomeHeader";
import AboutHome from "@/components/AboutHome";
import HomeServices from "@/components/HomeServices";
import HomeReviews from "@/components/HomeReviews";
import HomeProjects from "@/components/HomeProjects";
import HomeForms from "@/components/HomeForms";

export default {
  name: "HomeView",
  data() {
    return {};
  },
  components: {
    HomeProjects,
    HomeHeader,
    AboutHome,
    HomeServices,
    HomeReviews,
    HomeForms,
  },
  mixins: [updateTitle],
  created() {
    this.updateTitle(this.$t("main"));
  },
};
</script>

<style scoped lang="scss"></style>
