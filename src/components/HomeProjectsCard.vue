<template lang="pug">
div
  v-card(link elevation="0" @click="$router.push({ name: 'project', params: { slug: project.link_path } })" class="card rounded-xl pa-6" min-height="200")
    h3(class="white--text font-weight-bold mb-0") {{ project.title }}
    v-chip(class="white--text font-weight-bold px-4 pr-6" color="costumBlue")
      v-icon(class="mr-2") mdi-checkbook
      | {{ project.name }}
    div(class="category")
    div(class="white--text font-weight-bold")
      | Технологии:
      div(class="last pa-2") {{ project.stack  }}
</template>

<script>
export default {
  name: "HomeProjectsCard",
  props: {
    project: Object,
  },
};
</script>

<style scoped lang="scss">
.card {
  background-size: cover;
  background-repeat: no-repeat;
  background-image: url("../assets/images/card-two-background.jpg");
  transition: 0.2s all ease-in-out;
  display: flex;
  overflow: hidden;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: var(--shadow-2xl), 0 0 24px 0 rgba(255, 255, 255, 0.2) inset !important;
  transition: all 0.2s ease-in-out;

  &:hover {
    transition: 0.2s all ease-in-out;
    box-shadow: 0 6px 10px 0 rgba(0, 0, 0, 0.5) !important;
  }

  & > * {
    width: fit-content;
  }
}

.last {
  background-color: var(--custom-blue) !important;
  color: #fff;
  border-radius: 5px !important;
}

@media screen and (max-width: 600px) {
  .card {
    padding: 16px !important;
  }
}
</style>
