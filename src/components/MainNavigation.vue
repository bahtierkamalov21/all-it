<template lang="pug">
div
  nav(class="nav")
    v-container(fluid)
      v-col
        v-row(class="align-center")
          div(class="title")
            a(href="/") All IT.agency
              div(class="lang-prefix") {{ $i18n.locale }}
              div(class="tm") TM
          div(class="theme-button ml-8" icon @click="changeTheme")
            font-awesome-icon(v-if="!$vuetify.theme.dark" icon="fa-solid fa-earth-asia")
            div(v-if="$vuetify.theme.dark" class="icon-light-theme")
          switch-language(class="ml-6")
          v-spacer 
          div(class="logo")
            v-img(src="@/assets/logo.svg")
          ul
            li(v-for="item in links" :key="item.id" :class="item.list ? 'category-links' : null")
              router-link(:to="item.href" :class="item.list ? 'category-link pr-2' : null") {{ item.name }}
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-down
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-up
              div(v-if="item.list" class="link-list")
                router-link(v-for="list in item.list" :to="list.href" :key="list.id")
                  | {{ list.name }}
</template>

<script>
import SwitchLanguage from "./SwitchLanguage.vue";

export default {
  name: "MainNavigation",
  components: { SwitchLanguage },
  data() {
    return {
      links: [
        {
          name: "Поддержка",
          href: "#",
        },
        {
          name: this.$t("services"),
          href: "#",
          list: [
            {
              name: "Сайты",
              href: "sites",
            },
          ],
        },
        {
          name: "О компании",
          href: "#",
        },
        {
          name: "Отзывы",
          href: "#",
        },
        {
          name: this.$t("login"),
          href: "#",
        },
      ],
    };
  },
  methods: {
    changeTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    },
  },
};
</script>

<style scoped lang="scss">
.nav {
  background-color: #fff;

  & > *:first-child {
    display: flex;
    align-items: center;
    height: 56px;
    padding: 0 32px !important;
  }

  &-warning {
    overflow: hidden;
  }
}
.title {
  display: flex;
  align-items: center;
  font-family: "Poppins", "Roboto", sans-serif !important;
  font-size: 1.5rem !important;
  font-weight: 600;
  color: #666;

  & > *:first-child {
    position: relative;
    text-decoration: none;
    color: #666;
  }
}

.lang-prefix {
  position: absolute;
  right: -14px;
  top: -12px;
  color: #1e87f0;
  font-size: 13px;
  font-weight: 500;
}

.tm {
  position: absolute;
  top: -16px;
  left: 52px;
  font-size: 12px;
  font-weight: 500;
}

.hide {
  display: none;
}

ul {
  list-style: none;
  display: flex;
}

li {
  position: relative;

  & > * {
    text-decoration: none;
    transition: all 0.2s ease-in;
    font-weight: 500;
    display: flex;
    align-items: center;
    color: #999 !important;
    padding: 16px;
    padding-left: 0;
  }

  & > .category-link > *:first-child {
    display: block;
  }

  &:hover {
    & > .category-link > *:last-child {
      display: block;
    }

    & > .category-link > *:first-child {
      display: none;
    }

    & > * {
      transition: all 0.2s ease-in;
      color: #666 !important;
    }
  }
}

.icon-list {
  display: none;
  color: rgba(0, 0, 0, 0.54);
  position: relative;
  top: -2px;
}

.logo {
  height: 24px;
  width: 24px;
  border-radius: 10px;
  box-shadow: 0 5px 12px rgb(0 0 0 / 10%);
}

.category-links {
  &:hover {
    & > .link-list {
      display: block;
      animation: 0.2s hover-list-link ease-in-out;
    }
  }
}

.link-list {
  display: none;
  position: absolute;
  left: -16px;
  top: 56px;
  background-color: #fff;
  min-width: 200px;
  padding: 20px;
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

.active {
  display: block;
}

.icon-light-theme {
  background-color: yellow;
  height: 16px;
  width: 16px;
  border-radius: 50%;
  box-shadow: 0 0 12px 0 rgb(255 255 0 / 50%);
}

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

@keyframes hover-list-link {
  0% {
    opacity: 0.2;
  }
  100% {
    opacity: 1;
  }
}
</style>
