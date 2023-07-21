<template lang="pug">
div
  v-dialog(v-model="dialogProjectsLocal" hide-overlay width=600)
    div
      div(class="title font-weight-bold pl-6 mb-2") Добавить проект
      v-card(class="card rounded-lg pa-6" elevation="0")
        v-form(ref="form" v-model="valid" lazy-validation class="text-center" @submit.prevent="saveProject")
          div(class="d-flex flex-wrap" style="gap: 12px;")
            v-text-field(
              class="input"
              required
              v-model="projectTitle"
              :rules="[v => !!v || 'Поле должно быть заполнено']"
              solo 
              label="Заголовок проекта"
              type="text"
            )
            v-text-field(
              class="input"
              required
              v-model="projectName"
              :rules="[v => !!v || 'Поле должно быть заполнено']"
              solo 
              label="Название проекта"
              type="text"
            )
          div
            v-select(
              :items="categories"
              v-model="category"
              class="input"
              :rules="[v => !!v || 'Выберите категорию']"
              solo
              :menu-props="{ top: false, offsetY: true }"
              label="Категория"
            )
          div(class="mb-4")
            v-autocomplete(
              v-model="technology"
              :items="technologies"
              chips
              color="costumBlue"
              label="Технологии"
              full-width
              hide-details
              hide-no-data
              hide-selected
              multiple
              solo
              single-line
              class="input"
            )
              template(v-slot:selection="data")
                v-chip(
                  class="white--text"
                  v-bind="data.attrs"
                  :input-value="data.selected"
                  color="costumBlue"
                ) {{ data.item }}
          v-textarea(
            class="input mb-4"
            label="Описание проекта"
            solo
            v-model="description"
            hide-details
          )
          v-btn(
            @click="saveProject"
            color="costumBlue"
            class="white--text text-capitalize"
            elevation="0"
          )
            | Добавить
            span(class="text-lowercase ml-1") проект
</template>

<script>
import axios from "axios";

export default {
  name: "DilaogProjects",
  props: {
    dialogProjects: Boolean,
  },
  data: () => ({
    slug: null,
    technology: [],
    categories: [],
    description: null,
    objectsCategories: [],
    technologies: [],
    objectsTechnologies: [],
    category: null,
    valid: false,
    projectName: null,
    projectTitle: null,
  }),
  computed: {
    dialogProjectsLocal: {
      get() {
        return this.dialogProjects;
      },
      set(value) {
        this.$emit("getDialogProjects", value);
      },
    },
  },
  created() {
    this.getTechnologies();
    this.getCategories();
  },
  methods: {
    getTechnologies() {
      axios.get(this.$store.state.api_url + "stacks/").then((response) => {
        this.objectsTechnologies = response.data;
        this.technologies = response.data.map((item) => item.stack);
      });
    },
    projectApiSlug(text) {
      const slug = text.toLowerCase().replace(/\s+/g, "-");
      this.slug = slug;
    },
    getCategories() {
      axios.get(this.$store.state.api_url + "categories/").then((response) => {
        this.objectsCategories = response.data;
        this.categories = response.data.map((item) => item.title);
      });
    },
    checkCategory() {
      let url = null;

      this.objectsCategories.forEach((item) => {
        item.title === this.category ? (url = item.url) : null;
      });

      this.category = url;
    },
    checkTechnology() {
      let array = [];

      this.objectsTechnologies.forEach((item) => {
        this.technology.forEach((technology) => {
          technology === item.stack ? array.push(item.url) : null;
        });
      });

      this.technology = array;
    },
    saveProject() {
      const api = this.$store.state.api_url + "projects/";
      const fk_user = JSON.parse(localStorage.getItem("user")).url;

      this.projectName ? this.projectApiSlug(this.projectName) : null;

      this.checkTechnology();
      this.checkCategory();

      const data = {
        link_path: this.slug,
        stacks: this.technology,
        title: this.projectTitle,
        name: this.projectName,
        description: this.description,
        fk_user: fk_user,
        fk_category: this.category,
      };

      if (this.$refs.form.validate()) {
        axios.post(api, data).then(() => {
          // Отправка уведомления в телеграм
          const user = JSON.parse(localStorage.getItem("user"));
          let message = "<b>Уведомление: </b>\n";
          message += "<b>Добавлен новый проект от пользователя: </b>\n";
          message += `<b>telegram_username: ${user.telegram_username}</b>\n`;
          message += `<b>телефон: ${user.phone}</b>\n`;
          message += `<b>url проекта: ${this.$store.state.api_url}/projects/${this.slug}/</b>\n`;
          const api_url = `https://api.telegram.org/bot${this.$store.state.token}/sendMessage`;
          axios
            .post(api_url, {
              chat_id: this.$store.state.chat_id,
              parse_mode: "html",
              text: message,
            })
            .then(() => {
              location.reload();
            })
            .catch((errors) => {
              console.log(errors);
            });
        });
      }
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  box-shadow: var(--shadow-2xl) !important;
  overflow: auto;
  max-height: 60vh;
}

.title {
  color: #121133;
}
</style>
