<template lang="pug">
div
  v-dialog(v-model="accessDelete" hide-overlay width="440")
    v-card(
      class="card-dialog d-flex flex-column align-center justify-center pa-6 text-center rounded-xl" 
      style="gap: 12px;" 
      height="320" 
      width="100%"
    )
      div(class="title font-weight-bold") Вы точно хотите проект?
      v-icon(color="red" style="font-size: calc(var(--index) * 6);") mdi-delete
      div(class="d-flex" style="gap: 12px;")
        v-btn(
          class="text-capitalize font-weight-bold white--text" 
          color="red" 
          elevation="0"
          @click="deleteProject"
        ) Удалить
        v-btn(
          class="text-capitalize font-weight-bold" 
          elevation="0" 
          @click="accessDelete = false"
        ) Отмена
  v-card(elevation="0" class="card pa-2")
    div(class="d-flex align-center justify-space-between")
      div(class="d-flex align-center")
        v-chip(class="d-inline-flex font-weight-bold white--text align-center" color="costumBlue") Cтатус
          span(v-if="project.complete" class="status rounded-xl ml-2" :class="project.complete ? 'complete-color' : null")
          span(v-if="!project.complete" class="status rounded-xl ml-2" :class="project.status ? 'status-color' : 'green-color'")
        v-tooltip(right)
          template(v-slot:activator="{ on, attrs }")
            div(class="info-inf ml-2 rounded-xl" v-bind="attrs" v-on="on")
              v-icon mdi-information-variant
          span
            div(class="d-flex align-center") Статус
              span(class="status rounded-xl complete-color mx-2")
              | означает "Проект выполнен"
            div(class="d-flex align-center") Статус
              span(class="status rounded-xl status-color mx-2")
              | означает "Проект находится в ожидании выполнения"
            div(class="d-flex align-center") Статус
              span(class="status rounded-xl green-color mx-2")
              | означает "Проект находится в ожидании"
      v-btn(icon color="red" @click="accessDelete = true")
        v-icon mdi-delete
    v-card(class="pa-2 mt-2 rounded-tl-lg rounded-tr-lg")
      h3(class="ml-1 font-weight-bold mb-2") {{ project.title }}
      v-chip(class="d-inline-block white--text font-weight-bold px-4 pr-6" color="costumBlue")
        v-icon(class="mr-2") mdi-checkbook
        | {{ project.name }}
      br
      div(class="description my-2 rounded-lg font-weight-bold")
        div(class="pa-4") {{ project.description ? project.description : "Описания нет" }}
      div(class="font-weight-bold")
        span(class="ml-1") Технологии:
        br
        div(class="last pa-2 px-4 d-flex flex-wrap" style="width: fit-content; gap: 6px;")
          span(v-for="stack in project.stacks" :key="stack.url") {{ stack.stack }}
</template>

<script>
import axios from "axios";

export default {
  name: "ProfileProjectsCard",
  props: {
    project: Object,
  },
  data: () => ({
    accessDelete: false,
  }),
  methods: {
    deleteProject() {
      axios.delete(this.project.url).then(() => {
        this.accessDelete = false;
        location.reload();
      });
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  border: 1px solid #bdbdbd !important;
  border-radius: 20px !important;
  box-shadow: 0 0 24px 0 rgba(0, 0, 0, 0.05) inset !important;

  &-dialog {
    box-shadow: var(--shadow-2xl) !important;
    overflow: hidden;
  }
}

h3 {
  max-height: 56px;
  overflow: hidden;
  border-radius: 0 !important;
}

.last {
  background-color: var(--custom-blue) !important;
  color: #fff;
  border-radius: 20px !important;
}

.description {
  box-shadow: var(--shadow-lg) !important;
  height: 90px;
  max-height: 90px !important;
  overflow: auto;
}

.status {
  display: block;
  width: 10px;
  height: 10px;
}

.complete-color {
  background: lime;
}

.status-color {
  background: #ff5722;
}

.info-inf {
  background-color: #fff !important;
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.8);
}

.green-color {
  background: #78909c;
}
</style>
