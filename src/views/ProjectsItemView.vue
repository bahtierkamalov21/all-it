<template lang="pug">
div
  header(class="header py-16")
    v-container(class="container")
      v-col
        v-row(class="align-center")
          div(class="left")
            h1 {{ project.title }}
            h2 {{ project.name }}
          div(class="right")
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
import axios from "axios";

export default {
  name: "ProjectsItemView",
  mixins: [updateTitle],
  data() {
    return {
      project: {},
    };
  },
  created() {
    this.getProject();
  },
  methods: {
    getProject() {
      axios
        .get(this.$store.state.api_url + "projects/", {
          params: { link_path: this.$route.params },
        })
        .then((response) => {
          this.project = response.data[0];
          const arr = this.project.stack.split(" ");
          this.project.stack = arr;
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
}

.main {
  background-color: #212121;
  background-image: url("../assets/images/about-background.png");
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;
}

.container {
  min-height: inherit;

  & > *:first-child {
    min-height: inherit;

    & > *:first-child {
      min-height: inherit;
    }
  }
}

.stack {
  max-width: 720px;
}
</style>
