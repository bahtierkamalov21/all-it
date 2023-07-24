<template lang="pug">
div
  section(class="projects" id="projects")
    div(class="projects-wrapper")
      div
        shapes-home-header
      div
    v-container(class="container rounded-xl")
      router-link(to="/projects" class="text-decoration-none font-weight-medium") Последние проекты
      h2(class="white--text mb-4") Наши работы и кейсы
      home-projects-navigation(@sendProjects="getProjects")
      v-card(elevateion="0" class="rounded-xl pa-4 mt-6" ref="card")
        div(class="navigation d-flex justify-space-between mb-2")
          v-chip(color="primary pr-6")
            v-icon(class="status mr-2") mdi-star-check
            | Здесь представлены наши лучшие проекты и собственные разработки
          div(class="card-buttons")
            v-btn(
              elevation="0"
              class="pa-0 mr-2"
              min-width="48"
              @click="swiperProjects.slidePrev()"
              :disabled="disabledPrevSlide"
            )
              v-icon mdi-arrow-left
            v-btn(
              elevation="0" 
              class="pa-0" 
              min-width="48" 
              @click="swiperProjects.slideNext()"
              :disabled="disabledNextSlide"
            )
              v-icon mdi-arrow-right
        div(class="swiper-projects rounded-xl")
          div(class="swiper-wrapper")
            div(class="swiper-slide" v-for="project in projects" :key="project.url")
              home-projects-card(:project="project")
</template>

<script>
import ShapesHomeHeader from "./ShapesHomeHeader";
import HomeProjectsNavigation from "./HomeProjectsNavigation";
import HomeProjectsCard from "./HomeProjectsCard";
import { Swiper } from "swiper";

export default {
  name: "HomeProjects",
  components: { ShapesHomeHeader, HomeProjectsNavigation, HomeProjectsCard },
  data() {
    return {
      projects: [], // Проекты активной категории
      swiperProjects: null,
    };
  },
  computed: {
    disabledPrevSlide() {
      return this.swiperProjects ? this.swiperProjects.activeIndex === 0 : null;
    },
    disabledNextSlide() {
      if (this.swiperProjects) {
        return this.swiperProjects.activeIndex ===
          this.swiperProjects.slides.length - 1
          ? true
          : false;
      } else return null;
    },
  },
  methods: {
    getProjects(data) {
      // Очищаем swiper
      this.swiperProjects = null;

      // Только завершенные проекты
      this.projects = data.filter((item) => item.complete);

      // Инициализируем новый swiper
      this.swiperProjects = new Swiper(".swiper-projects", {
        slidesPerView: 1,
        spaceBetween: 10,
      });
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
    height: 720px;

    & > *:first-child {
      width: 50%;
      height: 100%;
      min-height: inherit;
      position: relative;
    }

    & > *:last-child {
      width: 50%;
      height: 100%;
    }
  }
}

.status {
  width: fit-content;
}

.swiper-projects {
  overflow: hidden;
}

.container {
  position: absolute;
  padding: 32px;
  width: 95%;
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow-2xl), 0 0 24px 0 rgba(255, 255, 255, 0.2) inset;

  & > *:first-child {
    font-size: 1.25rem;
    color: var(--custom-blue);
  }
}

.card {
  &-title {
    width: 80%;
  }
}

@media screen and (max-width: 1086px) {
  .container {
    width: 92.2%;
  }
}

@media screen and (max-width: 878px) {
  .projects {
    &-wrapper {
      height: 790px;

      & > *:first-child {
        height: 50%;
      }
    }
  }

  .navigation {
    flex-direction: column;
    gap: 12px;
  }

  .card {
    &-title {
      display: none;
    }
  }

  .container {
    padding: 18px;
    backdrop-filter: none;
  }
}

@media screen and (max-width: 600px) {
  .projects {
    &-wrapper {
      & > *:first-child {
        height: 10%;
      }
    }
  }
}
</style>
