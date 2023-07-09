<template lang="pug">
div
  v-card(class="rounded-xl" elevation="0" :style="shadow ? 'box-shadow: var(--shadow-lg) !important' : null")
    ul(class="d-flex align-center px-2 pb-2")
      li(class="mt-2")
        v-chip(@click="setActiveCategory(126, allProjects)" class="link mr-2" :class="{'active' : activeIndexCategory === 126}") Все проекты
      li(class="mt-2" v-for="(link, index) in links" :key="link.prefix")
        v-chip(@click="setActiveCategory(index, link.projects)" class="link mr-2" :class="{'active' : activeIndexCategory === index}") {{ link.title }}
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
      page: 1,
    };
  },
  props: {
    checkUrl: Boolean,
    shadow: Boolean,
  },
  created() {
    this.getCategoriesWithProjectsArray();
    this.getAllProjects();
  },
  watch: {
    $route: function () {
      this.checkUrlAndSetCategory();
    },
  },
  methods: {
    sendProjects() {
      this.$emit("sendProjects", this.projectsWithActiveIndexCategory);
    },
    sendPage() {
      this.$emit("sendPage", this.page);
    },
    checkUrlAndSetCategory() {
      this.sendPage();
      this.links.forEach((item, index) => {
        item.prefix === this.$route.params.slug
          ? this.setActiveCategory(index, item.projects)
          : null;
      });
    },
    setActiveCategory(index, array) {
      this.sendPage();
      const showAndSetProjects = () => {
        this.activeIndexCategory = index;
        this.projectsWithActiveIndexCategory = array;
        this.sendProjects();
      };
      let areArraysEqual =
        JSON.stringify(array) === JSON.stringify(this.allProjects);
      let arrayIsNotEmpty = array.length !== 0;
      if (arrayIsNotEmpty) {
        if (!areArraysEqual && !this.checkUrl) {
          showAndSetProjects();
        } else if (areArraysEqual && this.checkUrl) {
          showAndSetProjects();
          this.$route.path !== "/projects"
            ? this.$router.push("/projects")
            : null;
        } else if (!areArraysEqual && this.checkUrl) {
          showAndSetProjects();
          this.$route.params.slug !== this.links[index].prefix
            ? this.$router.push({
                name: "projectsCategory",
                params: { slug: this.links[index].prefix },
              })
            : null;
        } else if (areArraysEqual && !this.checkUrl) {
          showAndSetProjects();
        }
      }
    },
    getAllProjects() {
      axios
        .get(this.$store.state.api_url + "projects/")
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            const project = response.data[i];
            const stacks = [];
            const images = [];

            for (let j = 0; j < project.stacks.length; j++) {
              axios.get(project.stacks[j]).then((response) => {
                stacks.push(response.data);
              });
            }

            for (let j = 0; j < project.images.length; j++) {
              axios.get(project.images[j]).then((response) => {
                images.push(response.data);
              });
            }

            project.images = images;
            project.stacks = stacks;
          }

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
          for (let i = 0; i < response.data.length; i++) {
            const item = response.data[i];
            let projectsArray = [];

            for (let j = 0; j < item.projects.length; j++) {
              const project = item.projects[j];
              const stacks = [];
              const images = [];

              axios
                .get(project)
                .then((response) => {
                  if (Array.isArray(response.data.stacks)) {
                    for (let k = 0; k < response.data.stacks.length; k++) {
                      axios.get(response.data.stacks[k]).then((response) => {
                        stacks.push(response.data);
                      });
                    }
                  }

                  if (Array.isArray(project.images)) {
                    for (let k = 0; k < project.images.length; k++) {
                      axios.get(project.images[k]).then((response) => {
                        images.push(response.data);
                      });
                    }
                  }

                  response.data.images = images;
                  response.data.stacks = stacks;
                  projectsArray.push(response.data);
                })
                .catch((errors) => {
                  console.log(errors);
                });
            }

            item.projects = projectsArray;
            this.links.push(item);
          }
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
  },
};
</script>

<style scoped lang="scss">
ul {
  overflow: auto;
  position: relative;
}

ul::-webkit-scrollbar {
  display: none;
}

li {
  list-style: none;
}

.link {
  cursor: pointer;
}

.active {
  background-color: var(--custom-blue) !important;
  color: #fff;
}

@media screen and (max-width: 900px) {
  ul::before {
    position: absolute;
    width: 20px;
    height: 20px;
    background-color: rgba(255, 255, 255, 0.5);
    top: 0;
    right: 0;
  }
}
</style>
