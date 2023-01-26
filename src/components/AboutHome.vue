<template lang="pug">
div 
  section(class="about" id="#about-us")
    v-container(class="about-container")
      v-col
        v-row(class="justify-center align-center")
          v-card(class="about-card text-center rounded-lg")
            font-awesome-icon(icon="fa-solid fa-laptop-code" class="fa-3x white--text mb-4")
            h3(class="mb-4 white--text") Разработка
              br
              | IT-продуктов
            p(class="mb-6 white--text")
              | Наша команда с 2017 года профессионально занимается разработкой
              | IT-решений
            router-link(to="/about-us" class="text-decoration-none font-weight-bold white--text") Узнать больше
          v-card(class="about-card text-center rounded-lg")
            font-awesome-icon(icon="fa-solid fa-cloud" class="fa-3x white--text mb-4")
            h3(class="mb-4 white--text") Digital-решения
            p(class="mb-6 white--text")
              | Создаем и поддерживаем IT-решения различного уровня сложности,
              | включая Highload проекты. Поддерживаем проекты по формату Time &
              | Material.
            router-link(to="/about-us" class="text-decoration-none font-weight-bold white--text") Узнать больше
          v-card(class="about-card text-center rounded-lg")
            font-awesome-icon(icon="fa-solid fa-globe" class="fa-3x mb-4")
            h3(class="mb-4 font-weight-bold") IT-консалтинг
            p(class="mb-6")
              | Оказываем комплексный IT-консалтинг для наших клиентов (от стадии
              | прототипирования до полноценного выпуска продукта на рынок).
              | Поддерживаем проект после его сдачи.
            router-link(to="/about-us" class="text-decoration-none font-weight-bold") Узнать больше
</template>

<script>
export default {
  name: "AboutHome",
  props: {
    loading: Boolean,
  },
};
</script>

<style scoped lang="scss">
.about {
  background-color: #212121;
  background-image: url("../assets/images/about-background.png");
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;
  position: relative;
  overflow: hidden;

  &:before {
    content: "";
    background-color: var(--v-background-base);
    width: 130%;
    height: 100%;
    top: -80%;
    left: -20%;
    box-shadow: 0 0 24px 0 #000000;
    transform: rotate(-5deg);
    position: absolute;
  }

  &-container {
    & > *:first-child {
      height: 100%;

      & > *:first-child {
        height: 100%;
        padding-bottom: 6vh;

        & > * {
          background-size: cover;
          background-repeat: no-repeat;

          &:first-child {
            background-image: url("../assets/images/card-one-background.jpg");
          }

          &:nth-child(2) {
            background-image: url("../assets/images/card-two-background.jpg");
          }
        }
      }
    }
  }

  &-card {
    position: relative;
    min-height: 460px;
    max-width: 346px;
    margin: 15px;
    display: flex;
    align-items: center;
    flex-direction: column;
    padding: 46px 32px;
    justify-content: center;
    box-shadow: 6px 5px 30px 0 rgb(0 0 0 / 12%) !important;
    transition: all 0.5s ease;

    &:hover {
      box-shadow: 0 0 24px 0 rgb(255 255 255 / 20%) !important;
      transform: scale(1.02);
      transition: all 0.5s ease;
    }

    & > *:last-child {
      color: var(--v-color_shadow-base);
      text-decoration: none;
    }
  }
}

p {
  font-weight: 600;
}

@media screen and (max-width: 1086px) {
  .about {
    padding-bottom: 42px;

    &-container {
      & > *:first-child {
        & > *:first-child {
          padding-bottom: 0;
        }
      }
    }
  }
}

@media screen and (max-width: 600px) {
  .about {
    background-position: bottom !important;
    padding-bottom: 0;

    &:before {
      top: -92%;
      left: -25%;
      background-position: left;
    }

    &-card {
      padding: 32px;
      min-height: 376px;
    }
  }
}
</style>
