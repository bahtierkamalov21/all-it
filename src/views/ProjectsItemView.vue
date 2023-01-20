<template lang="pug">
div
  header(class="header")
    v-container(class="container")
      v-col(class="mb-12")
        v-row(class="align-center")
          div(class="left")
            h1 {{ project.title }}
            h2 {{ project.name }}
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
              v-card-text(class="white card-text pt-2") {{ item.description }}
</template>

<script>
import updateTitle from "@/mixins/updateTitle";
import Swiper from "swiper";
import axios from "axios";

export default {
  name: "ProjectsItemView",
  mixins: [updateTitle],
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
        .get(this.$store.state.api_url + "projects/", {
          params: { link_path: this.$route.params },
        })
        .then((response) => {
          const images = [];
          const stacks = [];
          response.data[0].images.forEach((item) => {
            axios.get(item).then((response) => {
              images.push(response.data.image);
            });
          });
          response.data[0].stacks.forEach((item) => {
            axios.get(item).then((response) => {
              stacks.push(response.data);
            });
          });
          this.project = response.data[0];
          this.project.images = images;
          this.project.stacks = stacks;
        });
    },
  },
};
</script>

<style scoped lang="scss">
.header {
  min-height: 50vh;
  overflow: hidden;
  padding-top: 126px;
  position: relative;
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

.container {
  min-height: inherit;
  position: relative;

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
}
</style>
