<template lang="pug">
div
  v-tooltip(bottom)
    template(v-slot:activator="{ on, attrs }")
      div(
        class="theme-button hide"
        @click="changeTheme"
        v-on="on"
      )
        font-awesome-icon(v-if="!$vuetify.theme.dark" icon="fa-solid fa-earth-asia")
        div(v-if="$vuetify.theme.dark" class="icon-light-theme")
    span Сменить тему
  div(
    class="theme-button mobile"
    @click="changeTheme"
  )
    font-awesome-icon(v-if="!$vuetify.theme.dark" icon="fa-solid fa-earth-asia")
    div(v-if="$vuetify.theme.dark" class="icon-light-theme")
</template>

<script>
export default {
  name: "SwitchTheme",
  methods: {
    changeTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
  },
};
</script>

<style scoped lang="scss">
.theme-button {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: rgba(0, 0, 0, 10%);
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;

  &:active {
    animation: 0.2s hover-list-link forwards;
  }

  & > *:first-child {
    color: #b2b2b2;
  }
}

.mobile {
  display: none;
}

.icon-light-theme {
  background-color: yellow;
  height: 16px;
  width: 16px;
  border-radius: 50%;
  box-shadow: 0 0 12px 0 rgb(255 255 0 / 50%);
}

@media screen and (max-width: 900px) {
  .hide {
    display: none;
  }

  .mobile {
    display: flex;
  }
}
</style>
