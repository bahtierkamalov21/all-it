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
          v-timeline-item(v-for="item in project.stack" :key="item.id")
            v-card(elevation="0" :color="addColorInTimeline(item)")
              v-card-title(class="white--text card-title") {{ item }}
              v-card-text(class="white card-text pt-2") {{ addTextInTimeline(item) }}
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
          let images = [];
          response.data[0].images.forEach((item) => {
            axios
              .get(item)
              .then((response) => {
                images.push(response.data.image);
              })
              .catch((errors) => {
                console.log(errors);
              });
          });
          this.project = response.data[0];
          this.project.images = images;
          const arr = this.project.stack.split(" ");
          this.project.stack = arr;
          console.log(this.project);
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
    addTextInTimeline(item) {
      switch (item) {
        case "Python":
          return "Python — высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ.";
        case "JavaScript":
          return "JavaScript — мультипарадигменный язык программирования. Поддерживает объектно-ориентированный, императивный и функциональный стили. Является реализацией спецификации ECMAScript. JavaScript обычно используется как встраиваемый язык для программного доступа к объектам приложений.";
        case "Docker":
          return "Docker — программное обеспечение для автоматизации развёртывания и управления приложениями в средах с поддержкой контейнеризации, контейнеризатор приложений.";
        case "Vue":
          return "Vue.js — JavaScript-фреймворк с открытым исходным кодом для создания пользовательских интерфейсов. Легко интегрируется в проекты с использованием других JavaScript-библиотек. Может функционировать как веб-фреймворк для разработки одностраничных приложений в реактивном стиле.";
        case "React":
          return "React — JavaScript-библиотека с открытым исходным кодом для разработки пользовательских интерфейсов. React разрабатывается и поддерживается Facebook, Instagram и сообществом отдельных разработчиков и корпораций. React может использоваться для разработки одностраничных и мобильных приложений.";
        case "Django":
          return "Django — свободный фреймворк для веб-приложений на языке Python, использующий шаблон проектирования MVC. Проект поддерживается организацией Django Software Foundation. Сайт на Django строится из одного или нескольких приложений, которые рекомендуется делать отчуждаемыми и подключаемыми.";
        case "Nginx":
          return "Nginx — веб-сервер и почтовый прокси-сервер, работающий на Unix-подобных операционных системах. Начиная с версии 0.7.52 появилась экспериментальная бинарная сборка под Microsoft Windows. Игорь Сысоев начал разработку в 2002 году. Осенью 2004 года вышел первый публично доступный релиз. ";
        case "Nodejs":
          return "Node или Node.js — программная платформа, основанная на движке V8, превращающая JavaScript из узкоспециализированного языка в язык общего назначения.";
      }
    },
    addColorInTimeline(item) {
      switch (item) {
        case "Python":
          return "green";
        case "Docker":
          return "blue";
        case "JavaScript":
          return "orange";
        case "Nginx":
          return "green";
        case "Vue":
          return "lime";
        case "Nodejs":
          return "#3e3f35";
        case "React":
          return "blue";
        case "Django":
          return "red";
      }
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
