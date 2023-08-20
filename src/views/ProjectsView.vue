<template lang="pug">
div(class="main")
  header(class="header pb-12")
    div
      v-container
        h1(class="pl-6 mb-2" style="color: #121133;") {{ $t("all") }}
          span(class="text-lowercase mx-2") {{ $t("projects-md") }}
          | /
          span(class="ml-1" style="font-size: 14px;") Выполнено проектов более 100+
        v-card(class="main-card rounded-xl ma-auto pb-6" max-width="1160")
          div(class="pa-4 navbar")
            home-projects-navigation(:shadow="true" @sendProjects="getProjects" checkUrl)
          div(class="ma-auto pa-6")
            loading-item(v-if="!projects.length")
            div(class="d-flex flex-column flex-wrap" v-else)
              home-projects-card(v-for="project in projects.slice(0, index_slice)" :key="project.url" :project="project")
          div(class="text-center")
            v-btn(@click="showMore()" :disabled="disabled" class="text-none" color="primary" rounded elevation="0") Показать ещё
</template>

<script>
// Components
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
      index_slice: 6,
      childrenActive: false,
      difference: null,
      projectsOnThisPage: null,
    };
  },
  components: { HomeProjectsCard, LoadingItem, HomeProjectsNavigation },
  mounted() {
    window.scrollTo(0, 0);
  },
  created() {
    this.updateTitle(this.$t("projects-md"));
  },
  computed: {
    disabled() {
      if (this.projects) {
        return this.projects.length < this.index_slice;
      } else return true;
    },
  },
  methods: {
    showMore() {
      this.index_slice += 6;
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
