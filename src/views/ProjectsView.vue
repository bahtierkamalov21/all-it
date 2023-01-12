<template lang="pug">
div(class="main")
  header(class="header pb-12")
    loading-item(v-if="!projects")
    div(v-else)
      v-container(v-if="childrenActive")
        router-view
      v-container(v-else)
        v-card(class="main-card rounded-xl")
          div
          div(class="pa-6")
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
    this.updateTitle(this.$t("projects-md"));
    this.getProjects();
  },
  methods: {
    getProjects() {
      axios
        .get(this.$store.state.api_url + "projects/")
        .then((response) => {
          this.projects = response.data.filter((item) => item.complete);
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
  },
};
</script>

<style scoped lang="scss">
.main {
  background-image: url("../assets/images/projects-background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  max-height: 2300px;
}

.header {
  padding-top: 126px;
}

.main-card {
  box-shadow: var(--shadow-2xl) !important;

  & > *:first-child {
    height: 100px;
    background: #eaf2ff;
  }
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}
</style>
