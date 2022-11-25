<template lang="pug">
div
  v-tooltip(bottom)
    template(v-slot:activator="{ on, attrs }")
      div(class="switch" @click="openList")
        div(v-bind="attrs" v-on="on")
          font-awesome-icon(icon="fa-solid fa-earth-asia" class="icon")
          div(class="ml-2") {{ $i18n.locale }}
          v-icon(class="chevron") {{ open ? "mdi-chevron-up" : "mdi-chevron-down" }}
        div(class="list-languages" v-if="open")
          ul
            li(v-for="item in listLanguages" :key="item.id" @click="changeLanguage(item)")
              | {{ item === "ru" ? (`Русский (${item.toUpperCase()})`) : null }}
              | {{ item === "en" ? (`Английский (${item.toUpperCase()})`) : null }}
    span Сменить язык
</template>

<script>
export default {
  name: "SwitchLanguage",
  data() {
    return {
      open: false,
      element: null,
      listLanguages: Object.getOwnPropertyNames(this.$i18n.messages),
    };
  },
  mounted() {
    this.element = document.querySelector(".switch");
    document.addEventListener("click", (event) => {
      const withinBoundaries = event.composedPath().includes(this.element);
      if (!withinBoundaries) {
        this.open = false;
      } else null;
    });
  },
  methods: {
    openList() {
      this.open = !this.open;
    },
    changeLanguage(lang) {
      this.$i18n.locale = lang;
    },
  },
};
</script>

<style scoped lang="scss">
.switch {
  border: 1px solid #999;
  border-radius: 20px;
  cursor: pointer;
  user-select: none;
  padding: 0 2px 0 6px;
  font-weight: 500;
  color: #999;
  position: relative;

  & > div {
    display: flex;
    align-items: center;

    & > *:nth-child(2) {
      text-transform: uppercase;
    }

    & > .icon {
      font-size: 14px !important;
    }
  }
}

.chevron {
  color: #999;
}

ul {
  list-style: none;
  padding: 0;
}

.list-languages {
  position: absolute;
  background-color: #fff;
  top: 56px;
  padding: 20px;
  min-width: 200px;
  left: -16px;
  border-radius: 10px;
  box-shadow: var(--base-shadow);

  & > * {
    text-decoration: none;
    color: #999 !important;
    transition: all 0.2s ease-in;

    &:hover {
      transition: all 0.2s ease-in;
      color: #666 !important;
    }
  }
}
</style>
