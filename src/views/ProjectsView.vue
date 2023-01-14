<template lang="pug">
div(class="main")
  header(class="header pb-12")
    loading-item(v-if="!projects")
    div(v-else)
      v-container
        v-card(class="main-card rounded-xl ma-auto pb-6" max-width="1160")
          div(class="pa-4")
            v-card-title(class="pa-2") Все проекты
            home-projects-navigation(@sendProjects="getProjects")
          div(class="ma-auto pa-6")
            div(class="d-flex flex-wrap" :class="addCenteredClass")
              home-projects-card(style="max-width: 336px; min-width: 336px;" v-for="project in forProjects" :key="project.url" :project="project")
          v-pagination(:length="lengthPages" v-model="page")
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import HomeProjectsCard from "@/components/HomeProjectsCard";
import LoadingItem from "@/components/LoadingItem";
import HomeProjectsNavigation from "@/components/HomeProjectsNavigation";

export default {
  name: "ProjectsView",
  mixins: [updateTitle],
  data() {
    return {
      projects: [],
      childrenActive: false,
      page: 1,
      page_copy: 1,
      sliceStart: 0,
      sliceEnd: 9,
      difference: null,
      projectsOnThisPage: null,
    };
  },
  components: { HomeProjectsCard, LoadingItem, HomeProjectsNavigation },
  mounted() {
    window.scrollTo(0, 0);
  },
  watch: {
    page() {
      if (this.page_copy < this.page) {
        this.sliceEnd = this.sliceEnd * this.page;
        this.sliceStart = this.sliceStart + 9;
        this.page_copy = this.page;
      } else {
        this.sliceEnd = this.sliceEnd / this.page_copy;
        this.sliceStart = this.sliceStart - 9;
        this.page_copy = this.page;
      }
    },
  },
  created() {
    this.updateTitle(this.$t("projects-md"));
  },
  computed: {
    lengthPages() {
      if (this.projects.length / 9 < 1 || this.projects.length / 9 > 1) {
        return Math.floor(this.projects.length / 9) + 1;
      } else return null;
    },
    addCenteredClass() {
      if (this.projectsOnThisPage > 1 && this.projectsOnThisPage % 3 != 0) {
        return "centered";
      } else if (this.projectsOnThisPage % 3 === 0) {
        return null;
      } else return null;
    },
    forProjects() {
      return this.projects.slice(this.sliceStart, this.sliceEnd);
    },
  },
  methods: {
    findingProjectsOnThisPage() {
      this.difference = (this.sliceEnd - this.projects.length) * 1;
      this.difference < 0 ? (this.difference = -this.difference) : null;
      this.projectsOnThisPage = this.projects.length - this.difference;
    },
    getProjects(data) {
      // Только завершенные проекты
      data ? (this.projects = data.filter((item) => item.complete)) : null;
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

.centered {
  justify-content: center;
}

.main-card {
  box-shadow: var(--shadow-2xl) !important;

  & > *:first-child {
    background: #eaf2ff;
  }

  & > *:nth-child(2) {
    max-width: 1080px;

    & > *:first-child {
      gap: 12px;
    }
  }
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }
}

@media screen and (max-width: 1126px) {
  .main-card {
    & > *:nth-child(2) {
      max-width: 732px;
    }
  }
}

@media screen and (max-width: 600px) {
  .main-card {
    & > *:nth-child(2) {
      padding: 8px !important;

      & > *:first-child {
        justify-content: center;
      }
    }
  }
}
</style>
