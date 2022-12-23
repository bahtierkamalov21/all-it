<template lang="pug">
div
  section(class="projects")
    div(class="projects-wrapper" ref="projectsWrapper")
      div
        shapes-home-header
      div
    v-container(class="container rounded-xl" ref="container")
      router-link(to="/projects" class="text-decoration-none font-weight-medium") Последние проекты
      h2(class="white--text mb-4") Наши работы и кейсы
      home-projects-navigation(@sendProjects="getProjects")
      v-card(elevateion="0" class="rounded-xl pa-4 mt-6" ref="card")
        div(class="swiper-projects")
          div(class="swiper-wrapper")
            div(class="swiper-slide" v-for="project in projects" :key="project.url")
              home-projects-card(:project="project")
</template>

<script>
import ShapesHomeHeader from "./ShapesHomeHeader";
import HomeProjectsNavigation from "./HomeProjectsNavigation";
import HomeProjectsCard from "./HomeProjectsCard";
import Swiper from "swiper";

export default {
  name: "HomeProjects",
  components: { ShapesHomeHeader, HomeProjectsNavigation, HomeProjectsCard },
  data() {
    return {
      allProjects: [],
      projects: [], // Проекты активной категории
      swiperProjects: null,
    };
  },
  mounted() {
    this.swiperProjects = new Swiper(".swiper-projects", {
      slidesPerView: 3,
      spaceBetween: 10,
      breakpoints: {
        320: {
          slidesPerView: 1,
        },
        640: {
          slidesPerView: 2,
        },
        1086: {
          slidesPerView: 3,
        },
      },
    });
    // First initilization media styles
    this.changeStyleElementsForMedia();
    // Resize window
    window.addEventListener("resize", () => {
      this.changeStyleElementsForMedia();
    });
  },
  methods: {
    getAllProjects() {},
    getProjects(data) {
      // Только завершенные проекты
      this.projects = data.filter((item) => item.complete);
    },
    changeStyleElementsForMedia() {
      this.$refs.projectsWrapper.style.minHeight = `${
        this.$refs.container.clientHeight + 380
      }px`;
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

  &-wrapper {
    width: 100%;
    display: flex;
    align-items: center;

    & > *:first-child {
      width: 50%;
      min-height: inherit;
      position: relative;
    }

    & > *:last-child {
      width: 50%;
    }
  }
}

.swiper-projects {
  overflow: hidden;
}

h2 {
  font-size: var(--section-title);
}

.container {
  position: absolute;
  padding: 32px;
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow-2xl), 0 0 24px 0 rgba(255, 255, 255, 0.2) inset;

  & > *:first-child {
    font-size: 1.25rem;
    color: var(--custom-blue);
  }
}

@media screen and (max-width: 1086px) {
  .container {
    width: 92.2%;
  }
}

@media screen and (max-width: 600px) {
  .container {
    padding: 18px;
    backdrop-filter: none;
  }
}
</style>
