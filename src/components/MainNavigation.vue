<template lang="pug">
div
  v-app-bar(class="nav-warning" dense elevation="0" color="#BAFC9D" :class="{ hide : this.$store.state.hideWarning }")
    div(class="ma-auto")
      strong Schema by Figma 2022. 
      | Register to attend our design systems conference virtually on November 16. Register today.
  nav(class="nav")
    v-container(fluid)
      v-col
        v-row(class="align-center")
          div(class="title")
            div All IT.Agency
          v-spacer 
          ul
            li(v-for="item in links" :key="item.id")
              router-link(:to="item.href") {{ item.name }}
</template>

<script>
export default {
  name: "MainNavigation",
  data() {
    return {
      links: [
        {
          name: "Gaming",
          href: "#",
        },
        {
          name: "Gaming",
          href: "#",
        },
      ],
    };
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
    border-radius: 8px;
    // box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.05) !important;
  }
}

.hide {
  display: none;
}

ul {
  list-style: none;
  display: flex;
  gap: 12px;
}

li {
  & > * {
    text-decoration: none;
    color: #000000ed !important;
    transition: all 0.2s ease-in;

    &:hover {
      opacity: 0.5;
      transition: all 0.2s ease-in;
    }
  }
}
</style>
