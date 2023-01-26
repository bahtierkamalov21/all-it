<template lang="pug">
div
  header
    home-header
  v-main
    about-home
    home-services
    home-reviews
    home-projects
    home-cost-sites
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
import HomeCostSites from "@/components/HomeCostSites";

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
    HomeCostSites,
  },
  mixins: [updateTitle],
  created() {
    this.updateTitle(this.$t("main"));
  },
  mounted() {
    window.scrollTo(0, 0);

    if (location.hash) {
      location.href = `/${location.hash}`;
    } else null;
  },
};
</script>

<style scoped lang="scss"></style>
