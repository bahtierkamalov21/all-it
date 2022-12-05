<template lang="pug">
div
  div(class="services-view pt-8 pb-6 text-center d-flex justify-center align-center rounded-lg")
    div(class="view")
      div(class="d-inline-block")
        div(id="services-one") 0
        font-awesome-icon(icon="fa-solid fa-plus")
      div Строк кода написано
    div(class="line")
    div(class="view")
      div(class="d-inline-block")
        div(id="services-two") 0
        font-awesome-icon(icon="fa-solid fa-plus")
      div Отзывов
    div(class="line")
    div(class="view")
      div(class="d-inline-block")
        div(id="services-tree") 0
        font-awesome-icon(icon="fa-solid fa-plus")
      div Партнеров
    div(class="line")
    div(class="view")
      div(class="d-inline-block")
        div(id="services-four") 0
        font-awesome-icon(icon="fa-solid fa-plus")
      div Проектов
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
  flex-wrap: wrap;
  background-image: url("../assets/images/services-views.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  left: 50%;
  width: 90%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
  gap: 46px;
  z-index: 10;
}

.line {
  width: 2px;
  height: 58px;
  background-color: #ffffff;
}

.view {
  color: #ffffff;

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

@media screen and (max-width: 600px) {
  .view {
    font-size: calc(var(--index) * 1.05);
    width: 20%;

    & > *:first-child {
      font-size: calc(var(--index) * 2);
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
