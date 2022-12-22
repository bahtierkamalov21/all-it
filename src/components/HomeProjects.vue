<template lang="pug">
div
  section(class="projects")
    div(class="projects-wrapper")
      div
        shapes-home-header
      div
    v-container(class="container rounded-xl my-16")
      router-link(to="/projects" class="text-decoration-none font-weight-medium") Последние проекты
      h2(class="white--text mb-4") Наши работы и кейсы
      home-projects-navigation(@sendProjects="getProjects")
      div(v-for="project in projects" :key="project.link_path") {{ project.title }}
</template>

<script>
import ShapesHomeHeader from "./ShapesHomeHeader";
import HomeProjectsNavigation from "./HomeProjectsNavigation";

export default {
  name: "HomeProjects",
  components: { ShapesHomeHeader, HomeProjectsNavigation },
  data() {
    return {
      projects: [],
    };
  },
  methods: {
    getProjects(data) {
      this.projects = data;
    },
  },
};
</script>

<style scoped lang="scss">
.projects {
  background-color: #212121;
  background-image: url("../assets/images/about-background.png");
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;
  position: relative;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;

  &-wrapper {
    width: 100%;
    display: flex;
    align-items: center;

    & > *:first-child {
      width: 50%;
      min-height: inherit;
      position: relative;

      & > .shapes {
      }
    }

    & > *:last-child {
      width: 50%;
    }
  }
}

h2 {
  font-size: var(--section-title);
}

.container {
  height: 80vh;
  position: absolute;
  padding: 32px;
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow-2xl);

  & > *:first-child {
    font-size: 1.25rem;
  }
}

@media screen and (max-width: 1086px) {
  .container {
    width: 92.2%;
  }
}
</style>
