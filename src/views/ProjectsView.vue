<template lang="pug">
div(class="main")
  header(class="header pb-12")
    loading-item(v-if="!projects")
    div(v-else)
      v-container(v-if="childrenActive")
        router-view
      v-container(v-else)
        v-card(class="main-card rounded-xl ma-auto pb-6" max-width="1160")
          div(class="d-flex")
          div(class="ma-auto pa-6")
            div(class="d-flex flex-wrap")
              home-projects-card(style="max-width: 336px; min-width: 336px;" v-for="project in forProjects" :key="project.url" :project="project")
          v-pagination(:length="lengthPages" v-model="page")
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
      page: 1,
      page_copy: 1,
      sliceStart: 0,
      sliceEnd: 9,
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
    this.getProjects();
  },
  computed: {
    lengthPages() {
      if (this.projects.length / 9 < 1 || this.projects.length / 9 > 1) {
        return Math.floor(this.projects.length / 9) + 1;
      } else return null;
    },
    forProjects() {
      return this.projects.slice(this.sliceStart, this.sliceEnd);
    },
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
