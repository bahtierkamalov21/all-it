<template lang="pug">
div
  header(class="header")
    loading-item(v-if="!projects")
    div(v-else)
      v-container(v-if="childrenActive")
        router-view
      v-container(v-else)
        v-card(class="main-card")
          home-projects-card(v-for="project in projects" :key="project.url" :project="project")
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeProjectsCard from "@/components/HomeProjectsCard";
import LoadingItem from "@/components/LoadingItem";
import axios from "axios";

export default {
  name: "ProjectsView",
  mixins: [updateTitle],
  data() {
    return {
      projects: null,
      childrenActive: false,
    };
  },
  components: { HomeProjectsCard, LoadingItem },
  mounted() {
    window.scrollTo(0, 0);
  },
  watch: {
    $route: function () {
      this.childrenActive = true;
    },
  },
  created() {
    this.getProjects();
  },
  methods: {
    getProjects() {
      axios
        .get(this.$store.state.api_url + "projects/")
        .then((response) => {
          this.projects = response.data;
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
  },
};
</script>

<style scoped lang="scss">
.header {
  padding-top: 126px;
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}
</style>
