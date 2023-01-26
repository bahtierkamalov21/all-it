<template lang="pug">
div
  nav(class="nav")
    top-sheet-menu(:open="sheetOpen" @setOpen="getOpen")
    v-container(class="container")
      v-col
        v-row(class="nav-row align-center")
          div(class="title")
            router-link(class="text-decoration-none" to="/") BMM LITER.org
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
              a(
                v-if="$route.path === '/'" 
                class="text-decoration-none" 
                :href="item.href" :class="item.list ? 'category-link pr-2' : null"
              ) {{ $t(item.name) }}
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-down
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-up
              router-link(
                v-else 
                class="text-decoration-none" 
                :to="'/' + item.href" 
                :class="item.list ? 'category-link pr-2' : null"
              ) {{ $t(item.name) }}
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-down
                v-icon(v-if="item.list" class="icon-list") mdi-chevron-up
              div(v-if="item.list" class="link-list" :class="item.list ? 'mr-2' : null")
                div
                  div(class="px-4" style="cursor: pointer;" v-for="list in item.list" @click="pushCategory(list.href)" :key="list.id")
                    | {{ list.name }}
          v-btn(v-if="!$store.state.user" class="text-capitalize font-weight-bold ml-4" elevation="0" rounded color="costumBlue")
            router-link(class="white--text text-decoration-none" to="/signup") {{ $t("login") }} / {{ $t("signup") }}
          v-btn(v-else class="text-capitalize font-weight-bold ml-4" elevation="0" rounded color="costumBlue")
            router-link(class="white--text text-decoration-none" to="/profile") {{ $t("personal-area") }}
</template>

<script>
import SwitchLanguage from "@/components/SwitchLanguage.vue";
import LogoItem from "@/components/LogoItem.vue";
import TopSheetMenu from "@/components/TopSheetMenu";
import SwitchTheme from "@/components/SwitchTheme";
import axios from "axios";

export default {
  name: "MainNavigation",
  components: { SwitchLanguage, SwitchTheme, LogoItem, TopSheetMenu },
  data() {
    return {
      sheetOpen: false,
      links: [
        {
          name: "support",
          href: "#support",
        },
        {
          name: "projects-md",
          href: "#projects",
          list: [],
        },
        {
          name: "about-company",
          href: "#services",
        },
        {
          name: "reviews",
          href: "#reviews",
        },
      ],
    };
  },
  watch: {
    sheetOpen() {
      this.sheetOpen
        ? (document.getElementsByTagName("html")[0].style.overflow = "hidden")
        : (document.getElementsByTagName("html")[0].style.overflow = "auto");
    },
  },
  created() {
    this.getCategoriesAndSetList();
  },
  methods: {
    getCategoriesAndSetList() {
      axios
        .get(this.$store.state.api_url + "categories/")
        .then((response) => {
          response.data.forEach((item) => {
            const object = {
              name: item.title,
              href: item.prefix,
            };
            this.links[1].list.push(object);
          });
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
    openSheet() {
      this.sheetOpen = !this.sheetOpen;
    },
    getOpen(callback) {
      this.sheetOpen = callback;
    },
    pushCategory(href) {
      this.$route.params.slug === href
        ? null
        : this.$router.push({
            name: "projectsCategory",
            params: { slug: href },
          });
    },
  },
};
</script>

<style scoped lang="scss">
.nav {
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
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

.account-icon {
  font-size: 2.2rem !important;
  position: relative;
  top: 1px;
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
    color: #666 !important;
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
      color: #999 !important;
    }
  }
}

.icon-list {
  display: none;
  color: #666;
  position: relative;
  top: -1px;
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
    padding: 8px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);

    & > * {
      color: #999 !important;
      border-radius: 8px;
      display: block;
      padding: 6px 0;
      margin-bottom: 8px;
      border: solid 2px transparent;
      transition: all 0.2s ease-in;
      box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.5);

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
}

.login-button {
  &-link {
    color: #fff !important;
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

@media screen and (max-width: 1142px) {
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
