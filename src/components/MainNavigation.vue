<template lang="pug">
div
  nav(class="nav")
    top-sheet-menu(:open="sheetOpen" @setOpen="getOpen")
    v-container(class="container")
      v-col
        v-row(class="nav-row align-center")
          div(class="title")
            router-link(class="text-decoration-none" to="/") All IT.agency
              div(class="lang-prefix") {{ $i18n.locale }}
              div(class="tm") TM
          div(class="bar")
            v-btn(icon @click="openSheet()")
             font-awesome-icon(icon="fa-solid fa-bars")
          switch-theme(class="ml-8")
          switch-language(class="mx-6")
          v-spacer
          logo-item
          ul
            li(v-for="item in links" :key="item.id" :class="item.list ? 'category-links' : null")
              router-link(class="text-decoration-none" :to="item.href" :class="item.list ? 'category-link pr-2' : null") {{ item.name }}
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-down
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-up
              div(v-if="item.list" class="link-list")
                div
                  router-link(class="text-decoration-none" v-for="list in item.list" :to="list.href" :key="list.id")
                    | {{ list.name }}
          div(class="login-signup ml-4")
            div
              router-link(class="text-decoration-none" to="/login") {{ $t("login") }} 
              v-icon mdi-account-circle
</template>

<script>
import SwitchLanguage from "@/components/SwitchLanguage.vue";
import LogoItem from "@/components/LogoItem.vue";
import TopSheetMenu from "@/components/TopSheetMenu";
import SwitchTheme from "@/components/SwitchTheme";

export default {
  name: "MainNavigation",
  components: { SwitchLanguage, SwitchTheme, LogoItem, TopSheetMenu },
  data() {
    return {
      sheetOpen: false,
      links: [
        {
          name: "Поддержка",
          href: "#",
        },
        {
          name: this.$t("projects-md"),
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
  watch: {
    sheetOpen() {
      if (this.sheetOpen) {
        document.getElementsByTagName("html")[0].style.overflow = "hidden";
      } else {
        document.getElementsByTagName("html")[0].style.overflow = "auto";
      }
    },
  },
  methods: {
    openSheet() {
      this.sheetOpen = !this.sheetOpen;
    },
    getOpen(callback) {
      this.sheetOpen = callback;
    },
  },
};
</script>

<style scoped lang="scss">
.nav {
  background-color: #e5e5e533;
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  padding: 12px;
  position: fixed;
  width: 100%;
  z-index: 120;

  &-warning {
    overflow: hidden;
  }
}

.container {
  padding: 0 24px;
  background-color: #fff;
  box-shadow: var(--shadow-lg);
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
    transition: all 0.2s ease-in;
    font-weight: 600;
    display: flex;
    align-items: center;
    color: #999 !important;
    height: 68px;
    padding: 0 16px 0 0;
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
    backdrop-filter: blur(16px);
    background-color: rgba(255, 255, 255, 10%);

    &:hover > *:first-child {
      transition: all 0.2s ease-in;
      color: var(--v-nav_link_hover-base) !important;
    }

    & > *:first-child {
      transition: all 0.2s ease-in;
      font-weight: 600;
      color: #999 !important;
    }
  }
}

.icon-list {
  display: none;
  color: rgba(0, 0, 0, 0.54);
  position: relative;
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

.bar {
  display: none;

  & > *:first-child {
    color: #212121 !important;
    font-size: 1.8rem !important;
    padding: 24px !important;
  }
}

@keyframes login-border {
  100% {
    transform: rotate(1turn);
  }
}

@media screen and (max-width: 960px) {
  .nav-row {
    height: 62px;
    justify-content: space-between;

    & > * {
      display: none;
    }

    & > *:first-child {
      display: block;
    }

    & > .bar {
      display: block;
    }
  }
}
</style>
