<template lang="pug">
div
  div(class="wrapper")
    section(class="services" id="services")
      v-container(class="pt-16 pb-16")
        v-col 
          v-row(class="justify-space-between align-center")
            h2(class="title")
              | На чем мы
              br
              | специализируемся?
            font-awesome-icon(icon="fa-solid fa-circle-check" class="subtitle")
        home-services-swiper(class="mt-16 mb-12")
    // Services View
    v-container(class="services__views")
      h3
        span(id="services-one")
        br
        span Строк кода написано
        font-awesome-icon(icon="fa-solid fa-plus")
      h3(id="two")
        span(id="services-two")
        br
        span Отзывов
        font-awesome-icon(icon="fa-solid fa-plus")
      h3(id="tree")
        span(id="services-tree")
        br
        span Подрядчиков
        font-awesome-icon(icon="fa-solid fa-plus")
      h3(id="four")
        span(id="services-four")
        br
        span Проектов
        font-awesome-icon(icon="fa-solid fa-plus")
</template>

<script>
import HomeServicesSwiper from "@/components/HomeServicesSwiper";

export default {
  name: "HomeServices",
  data() {
    return {
      show_transition_numbers: false,
      services: null,
    };
  },
  components: { HomeServicesSwiper },
  watch: {
    show_transition_numbers() {
      const services_one = document.getElementById("services-one");
      const services_two = document.getElementById("services-two");
      const services_tree = document.getElementById("services-tree");
      const services_four = document.getElementById("services-four");
      if (this.show_transition_numbers) {
        this.animation_numbers(services_one, 99000, 1000, 1500);
        this.animation_numbers(services_two, 95, 5, 5);
        this.animation_numbers(services_tree, 15, 2, 3);
        this.animation_numbers(services_four, 143, 1, 1);
      }
    },
  },
  mounted() {
    // Animation numbers
    this.services = document.querySelector(".services");

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((item) => {
        if (item.isIntersecting && !this.show_transition_numbers) {
          this.show_transition_numbers = true;
        } else null;
      });
    });

    observer.observe(this.services);
  },
  methods: {
    // Animation numbers
    animation_numbers(element, number, steps, counter) {
      let index = 0;
      let time = Math.round(4000 / (number / steps));
      let interval = setInterval(() => {
        index += counter;
        if (index === number) {
          clearInterval(interval);
        }
        element.innerHTML = index;
      }, time);
    },
  },
};
</script>

<style scoped lang="scss">
.wrapper {
  position: relative;
}

.title {
  font-size: 2.5rem !important;
  color: #ffffff;
  font-weight: 600;
  line-height: 2.5rem;
}

.subtitle {
  color: #ffffff;
  font-size: 3.5rem !important;
}

.services {
  height: 100%;
  position: relative;
  background-color: #323232;
  overflow: hidden;
  background-image: url("../assets/images/services-background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  box-shadow: 0 0 24px 0 rgba(0, 0, 0, 0.4);
  padding-bottom: 24px;

  &__views {
    display: flex;
    align-content: center;
    position: absolute;
    width: 1182px;
    background-image: url("../assets/images/services-views.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    padding-top: 52px;
    padding-bottom: 28px;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%);
    color: #ffffff;
    gap: 136px;
    justify-content: center;
    border-radius: 5px;
    text-align: center;
    z-index: 10;

    & > h3 {
      position: relative;
      & > span:first-child {
        font-size: 48px;
        line-height: 32px;
        font-weight: 600;
      }

      & > span {
        font-size: 16px;
        font-weight: 500;
      }

      & > *:last-child {
        position: absolute;
        font-size: 22px;
        top: -15px;
        right: -15px;
      }
    }

    & > *:nth-child(2) {
      &:before {
        content: "";
        background-color: #ffffff;
        height: 100%;
        width: 2px;
        position: absolute;
        right: -130%;
        top: -8px;
      }

      &:after {
        content: "";
        background-color: #ffffff;
        height: 100%;
        width: 2px;
        position: absolute;
        left: -95%;
        top: -8px;
      }

      & > *:last-child {
        position: absolute;
        font-size: 22px;
        top: -15px;
        right: -26px;
      }
    }

    & > *:nth-child(3) {
      &:before {
        content: "";
        background-color: #ffffff;
        height: 100%;
        width: 2px;
        position: absolute;
        right: -70%;
        top: -8px;
      }

      & > *:last-child {
        position: absolute;
        font-size: 22px;
        top: -15px;
        right: 0;
      }
    }

    & > *:last-child {
      & > *:last-child {
        position: absolute;
        font-size: 22px;
        top: -15px;
        right: -30px;
      }
    }
  }
}

@media screen and (max-width: 960px) {
  .services {
    &__views {
      gap: 0;
      justify-content: space-around;
      width: 90%;
      padding-right: 24px;

      & > h3 {
        &:nth-child(3) {
          &:before {
            right: -35%;
          }
        }

        &:nth-child(2) {
          &:before {
            right: -76%;
          }

          &:after {
            left: -50%;
          }
        }
      }
    }
  }
}

@media screen and (max-width: 780px) {
  .services {
    &__views {
      & > h3 {
        &:nth-child(2) {
          &:before {
            right: -70%;
          }

          &:after {
            left: -40%;
          }
        }
      }
    }
  }
}

@media screen and (max-width: 600px) {
  .title {
    font-size: 1.5rem !important;
    line-height: inherit !important;
  }
  .services {
    padding-bottom: 124px !important;

    & > *:first-child {
      padding-bottom: 0 !important;
    }

    &__views {
      padding-bottom: 25px !important;
      padding-left: 24px;
      padding-right: 12px;
      padding-top: 45px;
      display: grid !important;
      grid-template-columns: repeat(auto-fit, 50%);

      & > h3 {
        & > span:first-child {
          font-size: 32px !important;
        }
        & > span {
          font-size: 14px !important;
        }
      }

      & > *:nth-child(1) {
        margin-bottom: 40px;

        & > span {
          line-height: 2px;
        }

        & > *:last-child {
          right: 0 !important;
        }
      }

      & > *:nth-child(2) {
        margin-bottom: 40px;

        &:after {
          display: none;
        }

        &:before {
          display: none;
        }

        & > *:last-child {
          right: 30px !important;
        }
      }

      & > *:nth-child(3) {
        &:before {
          display: none;
        }

        & > *:last-child {
          right: 35px !important;
        }
      }

      & > *:nth-child(4) {
        & > *:last-child {
          right: 30px !important;
        }
      }
    }
  }
}
</style>
