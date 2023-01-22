<template lang="pug">
div
  v-card(class="card rounded-xl" elevation="0")
    ul(class="d-flex align-center px-2 pb-2")
      li(class="mt-2")
        v-chip(@click="setActiveCategory(126, allMyProjects)" class="mr-2" :class="{'active' : activeIndexCategory === 126}") Все проекты
      li(class="mt-2" v-for="link, index in links" :key="link.prefix")
        v-chip(@click="setActiveCategory(index, link.projects)" class="mr-2" :class="{'active' : activeIndexCategory === index}") {{ link.title }}
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileProjectsNavigation",
  data: () => ({
    allMyProjects: [],
    projectsWithActiveIndexCategory: [],
    activeIndexCategory: 126,
    links: [],
  }),
  created() {
    this.getAllMyProjects();
  },
  methods: {
    getCategoriesWithProjectsArray() {
      // Получим список категорий
      axios.get(this.$store.state.api_url + "categories/").then((response) => {
        // Создаем в объектах (категорий) новый массив с нашими проектами
        const myProjects = this.allMyProjects;

        response.data.forEach((category) => {
          const customProjectsArray = [];

          myProjects.forEach((project) => {
            project.fk_category === category.url
              ? customProjectsArray.push(project)
              : null;
          });

          category.projects = customProjectsArray;
        });
        this.links = response.data;
      });
    },
    getAllMyProjects() {
      const user_id = JSON.parse(localStorage.getItem("user")).id;

      axios
        .get(this.$store.state.api_url + "user_projects/", {
          params: {
            user_id: user_id,
          },
        })
        .then((response) => {
          response.data.forEach((project) => {
            const stacks = [];

            project.stacks.forEach((stack) => {
              axios.get(stack).then((response) => {
                stacks.push(response.data);
              });
            });

            project.stacks = stacks;
          });
          this.allMyProjects = response.data;

          // Отправляем проекты для категории "все проекты"
          this.allProjects = response.data;
          this.projectsWithActiveIndexCategory = this.allProjects;
          this.sendProjects();

          // Теперь получаем категории и добавляем в них наши проекты
          this.getCategoriesWithProjectsArray();
        });
    },
    setActiveCategory(index, array) {
      if (array.length) {
        this.activeIndexCategory = index;
        this.projectsWithActiveIndexCategory = array;
        this.sendProjects();
      }
    },
    sendProjects() {
      this.$emit("sendProjects", this.projectsWithActiveIndexCategory);
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  box-shadow: var(--shadow-lg) !important;
}

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
