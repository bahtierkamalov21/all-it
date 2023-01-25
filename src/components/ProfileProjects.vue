<template lang="pug">
div(v-if="projects.length")
  v-card(class="card rounded-xl ma-auto pb-4" max-width="960" elevation="0")
    profile-projects-navigation(@sendProjects="getProjects")
    div(class="pl-4 d-flex flex-wrap justify-space-between align-center")
      h3(class="ma-0") Мои проекты
      div(class="d-flex justify-end pa-4")
        v-btn(
          elevation="0"
          class="pa-0 mr-2"
          min-width="48"
          @click="swiperMyProjects.slidePrev()"
          :disabled="disabledPrevSlide"
        )
          v-icon mdi-arrow-left
        v-btn(
          elevation="0"
          class="pa-0" 
          min-width="48" 
          @click="swiperMyProjects.slideNext()"
          :disabled="disabledNextSlide"
        )
          v-icon mdi-arrow-right
    div(class="px-4")
      div(class="swiper-myprojects rounded-xl")
        div(class="swiper-wrapper")
          div(class="swiper-slide" v-for="project in projects" :key="project.url")
            profile-projects-card(:project="project")
</template>

<script>
import ProfileProjectsNavigation from "@/components/ProfileProjectsNavigation.vue";
import ProfileProjectsCard from "@/components/ProfileProjectsCard";
import { Swiper } from "swiper";

export default {
  name: "ProfileProjects",
  components: { ProfileProjectsNavigation, ProfileProjectsCard },
  data: () => ({
    projects: [],
    swiperMyProjects: null,
  }),
  computed: {
    disabledPrevSlide() {
      return this.swiperMyProjects
        ? this.swiperMyProjects.activeIndex === 0
        : null;
    },
    disabledNextSlide() {
      if (this.swiperMyProjects) {
        return this.swiperMyProjects.activeIndex ===
          this.swiperMyProjects.slides.length - 1
          ? true
          : false;
      } else return null;
    },
  },
  methods: {
    getProjects(value) {
      // Очиащем swiper
      this.swiperMyProjects = null;
      this.projects = value;
      // Инициализируем новый swiper
      this.swiperMyProjects = new Swiper(".swiper-myprojects", {
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
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  box-shadow: var(--shadow-2xl) !important;
  overflow: hidden !important;
}

.swiper-myprojects {
  overflow: hidden;
  border-radius: 0 !important;
}

.swiper-slide {
  width: 33%;
}

@media screen and (max-width: 1086px) {
  .swiper-slide {
    width: 50%;
  }
}

@media screen and (max-width: 878px) {
  .swiper-slide {
    width: 100%;
  }
}
</style>
