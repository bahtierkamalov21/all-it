<template lang="pug">
div
  v-card(link elevation="0" @click="$router.push({ name: 'project', params: { slug: project.link_path } })" class="card flex-wrap pa-6" min-height="200")
    div(class="left")
      div(class="ma-auto" style="width: fit-content;")
        h3(class="text-capitalize mb-2 font-weight-bold") {{ project.title }}
        div(class="description mb-6 font-weight-bold") {{ project.description }}
        v-chip(color="costumBlue" class="white--text stack px-4 pr-6 rounded-xl mb-2 font-weight-bold")
          div(class="mx-2" v-for="stack in project.stacks.slice(0, 2)" :key="stack.url") {{ stack.stack }}
          span(class="ml-2") ...
    div(class="right d-flex align-center justify-center")
      v-img(:src="imageSrc" class="image rounded-xl" max-width="300" height="160")
</template>

<script>
export default {
  name: "HomeProjectsCard",
  props: {
    project: Object,
  },
  computed: {
    imageSrc() {
      return this.project.images[0] ? this.project.images[0].image : null;
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  background-size: cover;
  background-repeat: no-repeat;
  background-image: url("../assets/images/card-two-background.jpg");
  transition: 0.2s all ease-in-out;
  border-radius: 24px !important;
  background-color: #0f182e;
  display: flex;
  overflow: hidden;
  justify-content: center;
  align-items: center;
  box-shadow: var(--shadow-2xl), 0 0 24px 0 rgba(255, 255, 255, 0.2) inset !important;
  transition: all 0.2s ease-in-out;
  gap: 12px;
  color: #fff;

  &:hover {
    transition: 0.2s all ease-in-out;
    box-shadow: 0 6px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  & > * {
    width: fit-content;
  }
}

.left {
  flex: 1 1 0%;
}

.right {
  flex: 1 1 0%;
}

.stack {
  display: flex;
  width: fit-content;
}

.description {
  max-width: 335px;
  height: 70px;
  overflow: hidden;
  color: var(--grey) !important;
}

@media screen and (max-width: 600px) {
  .image {
    max-width: 236px !important;
  }

  .left {
    & > *:first-child {
      text-align: start;
      margin-left: initial !important;
    }
  }
}
</style>
