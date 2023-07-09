<template lang="pug">
div
  header(class="header")
    div(class="header-wrapper")
      div
      div
        shapes-home-header
    v-container(class="header-container rounded-xl")
      div(class="mb-12 mt-6 d-flex justify-center" style="gap: 24px;")
        div(class="left")
          div(class="d-flex align-center mb-4")
            v-chip(
              color="costumBlue"
              class="name white--text font-weight-bold"
              style="box-shadow: var(--shadow-lg)"
            ) {{ project.name }}
          v-card(elevation="0" class="card-title rounded-lg pa-4 mb-6") 
            h2(class="text-capitalize") {{ project.title }}
          v-card(class="card-title d-inline-block pa-4 font-weight-bold py-2 rounded-lg mb-4" elevation="0") Дата завершения: 
          v-card(class="card-title pa-4 font-weight-bold rounded-lg py-2 d-inline-block ml-2") {{ project.data_complete }}
          div
            v-card-title(class="pa-0 pl-4 font-weight-bold") Описание
            v-card(elevation="0" class="card-title rounded-lg pa-4 pr-0") 
              div(class="font-weight-medium description pr-4") {{ project.description }}
        div(class="right")
          div(class="swiper-project-images rounded-xl")
            div(class="swiper-wrapper")
              div(v-for="image in project.images" class="swiper-slide")
                v-img(:src="image")
          div(class="text-right mt-4")
            v-chip(color="costumBlue white--text pr-4")
              v-icon(class="mr-2") mdi-credit-card-fast-outline
              | Свайпните слайд для просмотра следующей картинки
  div(class="stack-header white--text text-uppercase font-weight-bold text-center pt-6")
    | что мы использовали
    div(class="stack-decor mx-auto")
    div(class="stack-blur text-center text-uppercase font-weight-bold")
      div
  main(class="main")
    v-container
      div(class="stack mx-auto")
        v-timeline
          v-timeline-item(v-for="item in project.stacks" :key="item.id")
            v-card(elevation="0" :color="item.color")
              v-card-title(class="white--text card-title") {{ item.stack }}
              v-card-text(class="white black--text card-text pt-2") {{ item.description }}
      div(class="stack-card py-10 pb-0 px-4")
        v-card(class="mx-auto stack-card-card rounded-lg mb-10" elevation="0" v-for="item in project.stacks" :key="item.id")
          div(:style="{background: item.color}")
            v-card-title(class="white--text font-weight-bold card-title" :color="item.color") {{ item.stack }}
          v-card-text(class="white black--text card-text font-weight-bold  pt-2") {{ item.description }}
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import ShapesHomeHeader from "@/components/ShapesHomeHeader";
import Swiper from "swiper";
import axios from "axios";

export default {
  name: "ProjectsItemView",
  mixins: [updateTitle],
  components: { ShapesHomeHeader },
  data() {
    return {
      project: {},
      swiper_project_images: null,
    };
  },
  created() {
    this.getProject();
  },
  mounted() {
    window.scrollTo(0, 0);
    this.swiper_project_images = new Swiper(".swiper-project-images", {
      slidesPerView: 1,
    });
  },
  methods: {
    getProject() {
      axios
        .get(this.$store.state.api_url + "project_slug/", {
          params: { link_path: this.$route.params.slug },
        })
        .then((response) => {
          const images = [];
          const stacks = [];
          response.data.images.forEach((item) => {
            axios.get(item).then((response) => {
              images.push(response.data.image);
            });
          });
          response.data.stacks.forEach((item) => {
            axios.get(item).then((response) => {
              stacks.push(response.data);
            });
          });
          this.project = response.data;
          this.project.images = images;
          this.project.stacks = stacks;
        });
    },
  },
};
</script>

<style scoped lang="scss">
.header {
  padding-top: 126px;
  padding-bottom: 4vh !important;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  overflow: hidden;
  background-image: url("../assets/images/about-background.png");
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;

  &-wrapper {
    width: 100%;
    display: flex;
    align-items: center;
    height: 530px;
    max-width: 1160px;

    & > *:first-child {
      width: 50%;
      height: 100%;
    }

    & > *:last-child {
      width: 50%;
      height: 100%;
      min-height: inherit;
      position: relative;
    }
  }
}

h2 {
  font-size: 28px;
}

.description {
  overflow: auto;
  max-height: 140px;
}

.main {
  background-color: #212121;
  background-image: url("../assets/images/about-background.png");
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;
}

.left {
  width: 50%;
}

.right {
  width: 50%;
}

h1 {
  line-height: 38px;
}

.name {
  font-size: 24px;
  padding: 16px;
}

.header-container {
  position: absolute;
  backdrop-filter: blur(16px);
  box-shadow: var(--shadow-2xl), 0 0 24px 0 rgba(255, 255, 255, 0.2) inset;
  padding: 32px;
  padding-bottom: 26px;
  width: 95%;
  top: 112px;
  display: flex;
  justify-content: space-between;
  flex-direction: column;

  & > *:first-child {
    min-height: inherit;

    & > *:first-child {
      min-height: inherit;
    }
  }
}

.swiper-project-images {
  overflow: hidden;
  box-shadow: var(--shadow-2xl);
}

.stack {
  max-width: 720px;

  &-header {
    position: relative;
    overflow: hidden;
    padding-bottom: 18px;
    background-image: url("../assets/images/services-background.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    box-shadow: 0 0 24px 0 rgba(0, 0, 0, 0.5);
  }

  &-decor {
    width: 22px;
    height: 38px;
    border-radius: 20px;
    border: 1px solid #fff;
    margin-top: 10px;
    position: relative;
    overflow: hidden;

    &::before {
      content: "";
      position: absolute;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      transform: translate(-50%, 10%);
      background-color: #fff;
      animation: sparkling 4s ease-in-out infinite;
    }
  }

  &-blur {
    background-color: rgba(255, 255, 255, 0.15);
    filter: blur(52px);

    & > div {
      width: 200px;
      height: 200px;
      left: 50%;
      margin-right: -50%;
      transform: translate(-50%);
      border-radius: 50%;
      background-color: var(--custom-blue);
      position: absolute;
    }
  }
}

.stack-card {
  display: none;

  &-card {
    box-shadow: var(--shadow-lg) !important;
  }
}

.card-title {
  box-shadow: var(--shadow-lg) !important;
  width: fit-content !important;
}

@keyframes sparkling {
  0% {
    transform: translate(-50%, -150%);
  }

  50% {
    transform: translate(-50%, 10%);
  }

  80% {
    transform: translate(-50%, 10%);
  }

  100% {
    transform: translate(-50%, 250%);
  }
}

@media screen and (max-width: 1086px) {
  .header {
    padding-top: 106px;
  }

  .header-wrapper {
    height: 600px;
  }
}

@media screen and (max-width: 800px) {
  .stack {
    display: none;

    &-card {
      display: block;
    }
  }

  .header-wrapper {
    height: 990px;
  }

  .header-container {
    padding: 0 24px !important;
    backdrop-filter: none;

    & > *:first-child {
      display: block !important;
    }
  }

  .left {
    width: 100%;
    margin-bottom: 28px;
  }

  .right {
    width: 100%;
  }
}

@media screen and (max-width: 600px) {
  .description {
    max-height: 100px;
  }

  .header-wrapper {
    height: 780px;
  }

  .header-container {
    padding: 0 20px !important;
  }
}
</style>
