<template lang="pug">
div 
  section(class="about" id="#about-us")
    v-container(class="pa-0 about__container")
      v-col
        v-row(class="justify-center align-center")
          v-card(class="text-center about__card" min-width="25%")
            font-awesome-icon(icon="fa-solid fa-laptop-code" class="fa-3x mb-4")
            h3(class="mb-4") Разработка и продвижение IT-продуктов
            p(class="mb-8")
              | Наша команда с 2017 года профессионально занимается разработкой
              | IT-решен
            router-link(to="/about-us") Узнать больше
          v-card(class="text-center about__card" min-width="25%")
            font-awesome-icon(icon="fa-solid fa-cloud" class="fa-3x mb-4")
            h3 Digital-решения
            p
              | Создаем и поддерживаем IT-решения различного уровня сложности,
              | включая Highload проекты. Поддерживаем проекты по формату Time &
              | Material.
            router-link(to="/about-us") Узнать больше
          v-card(class="text-center about__card" min-width="25%")
            font-awesome-icon(icon="fa-solid fa-globe" class="fa-3x mb-4")
            h3 IT-консалтинг
            p
              | Оказываем комплексный IT-консалтинг для наших клиентов (от стадии
              | прототипирования до полноценного выпуска продукта на рынок).
              | Поддерживаем проект после его сдачи.
            router-link(to="/about-us") Узнать больше
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

  &__container {
    & > *:first-child {
      height: 100%;

      & > *:first-child {
        height: 100%;
        padding-bottom: 6vh;

        & > *:nth-child(1) {
          background-image: url("../assets/images/card-one-background.jpg");
          background-size: cover;
          background-repeat: no-repeat;
          color: #ffffff;

          & > *:last-child {
            color: #ffffff;
            text-decoration: none;
          }
        }

        & > *:nth-child(2) {
          background-image: url("../assets/images/card-two-background.jpg");
          background-size: cover;
          background-repeat: no-repeat;
          color: #ffffff;

          & > *:last-child {
            color: #ffffff;
            text-decoration: none;
          }
        }
      }
    }
  }

  &__card {
    position: relative;
    width: 30%;
    min-height: 460px;
    margin: 15px;
    padding: 84px 45px 77px !important;
    box-shadow: 6px 5px 30px 0 rgb(0 0 0 / 12%) !important;
    border-radius: 5px !important;
    transition: all 0.5s ease;

    &:hover {
      box-shadow: 0 0 24px 0 rgb(255 255 255 / 20%) !important;
      transform: scale(1.02);
      transition: all 0.5s ease;
    }

    & > h3 {
      font-size: 18px;
      margin-bottom: 14px;
    }

    & > p {
      font-size: 14px;
      line-height: 26px;
    }

    & > *:last-child {
      color: var(--v-color_shadow-base);
      text-decoration: none;
    }
  }
}

@media screen and (max-width: 900px) {
  .about {
    padding-bottom: 42px;

    &__card {
      min-width: 40% !important;
    }
  }
}

@media screen and (max-width: 600px) {
  .about {
    background-position: bottom !important;

    &:before {
      top: -92%;
      left: -45%;
      background-position: left;
    }
    &__card {
      width: 80%;
    }
  }
}
</style>
