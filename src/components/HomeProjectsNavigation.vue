<template lang="pug">
div
  v-card(class="rounded-xl" elevation="0")
    ul(class="d-flex flex-wrap align-center px-2 pb-2")
      li(class="mt-2")
        v-chip(@click="setActiveCategory(126, allProjects)" class="mr-2" :class="{'active' : activeIndexCategory === 126}") Все проекты
      li(class="mt-2" v-for="link, index in links" :key="link.prefix")
        v-chip(@click="setActiveCategory(index, link.projects)" class="mr-2" :class="{'active' : activeIndexCategory === index}") {{ link.title }}
</template>

<script>
import axios from "axios";

export default {
  name: "HomeProjectsNavigation",
  data() {
    return {
      links: [],
      allProjects: [],
      projectsWithActiveIndexCategory: [],
      activeIndexCategory: 126,
    };
  },
  created() {
    this.getCategoriesWithProjectsArray();
    this.getAllProjects();
  },
  methods: {
    sendProjects() {
      this.$emit("sendProjects", this.projectsWithActiveIndexCategory);
    },
    setActiveCategory(index, array) {
      if (array.length) {
        this.activeIndexCategory = index;
        this.projectsWithActiveIndexCategory = array;
        this.sendProjects();
      }
    },
    getAllProjects() {
      axios
        .get(this.$store.state.api_url + "projects/")
        .then((response) => {
          this.allProjects = response.data;
          this.projectsWithActiveIndexCategory = this.allProjects;
          this.sendProjects();
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
    getCategoriesWithProjectsArray() {
      axios
        .get(this.$store.state.api_url + "categories/")
        .then((response) => {
          response.data.forEach((item) => {
            let projectsArray = [];
            item.projects.forEach((project) => {
              axios
                .get(project)
                .then((response) => {
                  projectsArray.push(response.data);
                })
                .catch((errors) => {
                  console.log(errors);
                });
            });
            item.projects = projectsArray;
            this.links.push(item);
          });
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
  },
};
</script>

<style scoped lang="scss">
li {
  list-style: none;
}

.active {
  background-color: var(--custom-blue) !important;
  color: #fff;
}
</style>
