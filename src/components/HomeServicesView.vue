<template lang="pug">
div
  div(class="services-view text-center rounded-lg")
    v-container(class="pt-8 pb-6")
      v-col
        v-row(class="v-row justify-space-between align-center")
          div(class="view white--text")
            div(class="d-inline-block")
              div(id="services-one" class="font-weight-medium") 0
              font-awesome-icon(icon="fa-solid fa-plus")
            div(class="font-weight-medium") Строк кода написано
          div(class="line white")
          div(class="view white--text")
            div(class="d-inline-block")
              div(id="services-two" class="font-weight-medium") 0
              font-awesome-icon(icon="fa-solid fa-plus")
            div(class="font-weight-medium") Отзывов
          div(class="line white")
          div(class="view white--text")
            div(class="d-inline-block")
              div(id="services-tree" class="font-weight-medium") 0
              font-awesome-icon(icon="fa-solid fa-plus")
            div(class="font-weight-medium") Подрядчиков
          div(class="line white")
          div(class="view white--text")
            div(class="d-inline-block")
              div(id="services-four" class="font-weight-medium") 0
              font-awesome-icon(icon="fa-solid fa-plus")
            div(class="font-weight-medium") Проектов
</template>

<script>
export default {
  name: "HomeServicesView",
  data() {
    return {
      show_transition_numbers: false,
      element: null,
    };
  },
  watch: {
    show_transition_numbers() {
      const services_one = document.getElementById("services-one");
      const services_two = document.getElementById("services-two");
      const services_tree = document.getElementById("services-tree");
      const services_four = document.getElementById("services-four");
      if (this.show_transition_numbers) {
        this.animation_numbers(services_one, 99000, 1000, 1000);
        this.animation_numbers(services_two, 95, 1, 1);
        this.animation_numbers(services_tree, 15, 1, 1);
        this.animation_numbers(services_four, 143, 1, 1);
      } else null;
    },
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
  mounted() {
    // Animation numbers
    this.element = document.querySelector(".services-view");
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((item) => {
        if (item.isIntersecting && !this.show_transition_numbers) {
          this.show_transition_numbers = true;
        } else null;
      });
    });
    observer.observe(this.element);
  },
};
</script>

<style scoped lang="scss">
.services-view {
  position: absolute;
  background-image: url("../assets/images/services-views.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  left: 50%;
  max-width: 1156px;
  width: 90%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
  z-index: 2;

  & > div {
    max-width: 680px;
  }
}

.line {
  width: 2px;
  height: 58px;
}

.view {
  & > *:first-child {
    position: relative;
    font-size: 1.875rem;

    & > *:last-child {
      position: absolute;
      position: absolute;
      right: -18px;
      top: -12px;
      font-size: initial;
    }
  }
}

@media screen and (max-width: 768px) {
  .v-row {
    justify-content: space-around !important;
  }
}

@media screen and (max-width: 600px) {
  .view {
    font-size: calc(var(--index) * 1.25);
    width: 35%;

    & > *:first-child {
      font-size: calc(var(--index) * 2.2);
    }
  }

  .v-row {
    gap: 24px;
    position: relative;

    &::before {
      content: "";
      height: 100%;
      width: 2px;
      position: absolute;
      top: 0;
      left: 52%;
      margin-right: -50%;
      transform: translateX(-40%);
    }
  }

  .line {
    display: none;
  }

  .services-view {
    gap: initial;
    justify-content: space-around !important;
    padding-left: 12px;
    padding-right: 12px;
  }
}
</style>
