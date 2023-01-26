<template lang="pug">
div(class="main")
  header(class="header pb-12")
    loading-item(v-if="!projects")
    div(v-else)
      v-container
        h1(class="pl-6 mb-2" style="color: #121133;") {{ $t("all") }}
          span(class="text-lowercase mx-2") {{ $t("projects-md") }}
          | /
          span(class="ml-1" style="font-size: 14px;") Выполнено проектов более 100+
        v-card(class="main-card rounded-xl ma-auto pb-6" max-width="1160")
          div(class="pa-4 navbar")
            home-projects-navigation(:shadow="true" @sendProjects="getProjects" @sendPage="getPage" checkUrl)
          div(class="ma-auto pa-6")
            div(class="d-flex flex-column flex-wrap")
              home-projects-card(v-for="project in forProjects" :key="project.url" :project="project")
          v-pagination(circle :length="lengthPages" v-model="page")
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
      sliceEnd: 6,
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
        this.sliceStart = this.sliceStart + 6;
        this.page_copy = this.page;
      } else {
        this.sliceEnd = this.sliceEnd / this.page_copy;
        this.sliceStart = this.sliceStart - 6;
        this.page_copy = this.page;
      }
    },
  },
  created() {
    this.updateTitle(this.$t("projects-md"));
  },
  computed: {
    lengthPages() {
      if (this.projects.length / 6 < 1 || this.projects.length / 6 > 1) {
        return Math.floor(this.projects.length / 6) + 1;
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
    getPage(data) {
      this.page = data;
    },
  },
};
</script>

<style scoped lang="scss">
.main {
  background-image: url("../assets/images/projects-background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
}

.header {
  padding-top: 126px;
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

h1 {
  font-size: 38px;
  line-height: initial;
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
      & > *:first-child {
        justify-content: center;
      }
    }
  }

  h1 {
    line-height: 20px;
  }
}
</style>
