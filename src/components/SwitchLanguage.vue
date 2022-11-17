<template lang="pug">
div
  div(class="switch" @click="openList")
    font-awesome-icon(icon="fa-solid fa-earth-asia" class="icon")
    div(class="ml-2") {{ $i18n.locale }}
    v-icon(class="chevron") {{ open ? "mdi-chevron-up" : "mdi-chevron-down" }}
    div(class="list-languages" v-if="open")
      ul
        li(v-for="item in listLanguages" :key="item.id" @click="changeLanguage(item)")
          | {{ item === "ru" ? (`Русский (${item.toUpperCase()})`) : null }}
          | {{ item === "en" ? (`Английский (${item.toUpperCase()})`) : null }}
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
  display: flex;
  align-items: center;
  cursor: pointer;
  user-select: none;
  padding: 0 2px 0 6px;
  font-weight: 500;
  color: #999;
  position: relative;
  & > *:nth-child(2) {
    text-transform: uppercase;
  }

  & > .icon {
    font-size: 14px !important;
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
  top: 40px;
  padding: 20px;
  min-width: 200px;
  left: -16px;
  box-shadow: 0 5px 12px rgb(0 0 0 / 15%);

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
