<template lang="pug">
div
  v-tooltip(bottom)
    template(v-slot:activator="{ on, attrs }")
      div(class="switch" ref="switch" @click="openList")
        div(v-bind="attrs" v-on="on")
          font-awesome-icon(icon="fa-solid fa-earth-asia" class="icon")
          div(class="ml-2") {{ $i18n.locale }}
          v-icon(class="chevron") {{ open ? "mdi-chevron-up" : "mdi-chevron-down" }}
        div(class="list-languages" v-if="open")
          ul
            li(v-for="item in listLanguages" :key="item.id" class="align-center px-4" @click="changeLanguage(item)")
              flag(:iso="item" class="mr-2 rounded-xl" v-if="item != 'en'")
              flag(iso="us" class="mr-1 rounded-xl" v-else)
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
      listLanguages: Object.getOwnPropertyNames(this.$i18n.messages),
    };
  },
  mounted() {
    document.addEventListener("click", (event) => {
      const withinBoundaries = event.composedPath().includes(this.$refs.switch);
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
  padding: 8px;
  z-index: 10;
  width: max-content;
  left: -16px;
  border-radius: 10px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);

  & > ul > * {
    text-decoration: none;
    color: #999 !important;
    transition: all 0.2s ease-in;
    box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.5);
    padding: 6px 0;
    margin-bottom: 8px;
    border-radius: 8px;
    border: solid 2px transparent;

    &:last-child {
      margin: 0;
    }

    &:hover {
      transition: all 0.2s ease-in;
      color: #666 !important;
      box-shadow: 0 4px 2px 0 rgba(0, 0, 0, 0.2);
      border-color: #999;
    }
  }
}
</style>
