<template lang="pug">
div
  nav(class="nav")
    v-container(class="container")
      v-col
        v-row(class="align-center")
          div(class="title")
            a(href="/") All IT.agency
              div(class="lang-prefix") {{ $i18n.locale }}
              div(class="tm") TM
          v-tooltip(bottom)
            template(v-slot:activator="{ on, attrs }")
              div(
                class="theme-button ml-8" 
                icon 
                @click="changeTheme"
                v-on="on"
              )
                font-awesome-icon(v-if="!$vuetify.theme.dark" icon="fa-solid fa-earth-asia")
                div(v-if="$vuetify.theme.dark" class="icon-light-theme")
            span Сменить тему
          switch-language(class="ml-6")
          v-spacer
          logo-item
          ul
            li(v-for="item in links" :key="item.id" :class="item.list ? 'category-links' : null")
              router-link(:to="item.href" :class="item.list ? 'category-link pr-2' : null") {{ item.name }}
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-down
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-up
              div(v-if="item.list" class="link-list")
                div
                  router-link(v-for="list in item.list" :to="list.href" :key="list.id")
                    | {{ list.name }}
          div(class="login-signup ml-4")
            div
              router-link(to="/login") {{ $t("login") }} 
              v-icon mdi-account-circle
</template>

<script>
import SwitchLanguage from "./SwitchLanguage.vue";
import LogoItem from "./LogoItem.vue";

export default {
  name: "MainNavigation",
  components: { SwitchLanguage, LogoItem },
  data() {
    return {
      links: [
        {
          name: "Поддержка",
          href: "#",
        },
        {
          name: "Проекты",
          href: "/projects",
        },
        {
          name: this.$t("services"),
          href: "#",
          list: [
            {
              name: "Сайты",
              href: "projects/category/sites",
            },
            {
              name: "Telegram Боты",
              href: "projects/category/telegram-bots",
            },
            {
              name: "PWA",
              href: "projects/category/pwa",
            },
            {
              name: "Моб приложения",
              href: "projects/category/mobile-apps",
            },
            {
              name: "Автоматизации",
              href: "projects/category/automation",
            },
            {
              name: "DevOps",
              href: "projects/category/devops",
            },
            {
              name: "Серверное администрирование",
              href: "projects/category/server-administration",
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
      ],
    };
  },
  methods: {
    changeTheme() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      this.$store.commit("changeTheme", this.$vuetify.theme.dark);
    },
  },
};
</script>

<style scoped lang="scss">
.nav {
  background-color: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  padding: 12px 12px 0 12px;
  position: fixed;
  width: 100%;
  z-index: 10;

  &-warning {
    overflow: hidden;
  }
}

.container {
  padding: 0 24px;
  background-color: #fff;
  box-shadow: var(--base-shadow);
  max-width: 1366px;
  border-radius: 10px;
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

  & > *:last-child > a {
    padding: 0;
  }
}

li {
  position: relative;

  & > * {
    text-decoration: none;
    transition: all 0.2s ease-in;
    font-weight: 600;
    display: flex;
    align-items: center;
    color: #999 !important;
    padding: 0 16px;
    height: 68px;
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

.login-signup {
  background-color: var(--v-background-base);
  border-radius: 20px;
  height: 42px;
  min-width: 108px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(0, 0, 0, 5%);
  overflow: hidden;
  position: relative;

  &::before {
    content: "";
    position: absolute;
    left: -50%;
    top: -50%;
    width: 200%;
    height: 200%;
    background-color: var(--v-background-base);
    background-repeat: no-repeat;
    background-size: 50% 50%, 50% 50%;
    background-position: 0 0, 100% 0, 100% 100%, 0 100%;
    background-image: linear-gradient(
        var(--v-background-base),
        var(--v-background-base)
      ),
      linear-gradient(#337ab7, #337ab7),
      linear-gradient(var(--v-background-base), var(--v-background-base)),
      linear-gradient(#337ab7, #337ab7);
    animation: login-border 4s linear infinite;
  }

  &::after {
    content: "";
    width: calc(100% - 4px);
    height: calc(100% - 4px);
    background-color: var(--v-background-base);
    position: absolute;
    left: 2px;
    top: 2px;
    border-radius: 20px;
    z-index: 2;
  }

  & > div {
    gap: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 12px;
    width: 100%;
    position: relative;
    z-index: 4;
    height: 100%;
    backdrop-filter: 16px;
    background-color: rgba(255, 255, 255, 10%);

    &:hover > *:first-child {
      transition: all 0.2s ease-in;
      color: var(--v-nav_link_hover-base) !important;
    }

    & > *:first-child {
      transition: all 0.2s ease-in;
      font-weight: 600;
      color: #999 !important;
      text-decoration: none;
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
  height: 38px;
  width: 38px;
  border-radius: 8px;
  box-shadow: 0 0 5px 0 rgb(0 0 0 / 10%);
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
  top: 68px;
  min-width: 200px;
  padding-top: 10px;

  & > div {
    position: relative;
    background-color: #fff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: var(--base-shadow);

    & > * {
      text-decoration: none;
      color: #999 !important;
      display: block;
      transition: all 0.2s ease-in;

      &:hover {
        transition: all 0.2s ease-in;
        color: #666 !important;
      }
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

@keyframes login-border {
  100% {
    transform: rotate(1turn);
  }
}

@keyframes hover-list-link {
  from {
    opacity: 0.2;
  }

  to {
    opacity: 1;
  }
}
</style>
