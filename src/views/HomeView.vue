<template lang="pug">
div
  header
    home-header
  main
    about-home
    home-services
    home-reviews
    home-projects
    the-faq
  footer
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeHeader from "@/components/HomeHeader";
import AboutHome from "@/components/AboutHome";
import HomeServices from "@/components/HomeServices";
import HomeReviews from "@/components/HomeReviews";
import HomeProjects from "@/components/HomeProjects";
import TheFaq from "@/components/TheFaq";

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
    TheFaq,
  },
  mixins: [updateTitle],
  created() {
    this.updateTitle(this.$t("main"));
  },
};
</script>

<style scoped lang="scss"></style>
