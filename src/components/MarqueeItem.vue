<template lang="pug">
div
  div(class="marquee") 
    ul
      li(v-for="item in images" :key="item.id" style="width: 120px; height: 60px;")
        v-img(:src="item.image")
</template>

<script>
export default {
  name: "MarqueeItem",
  data() {
    return {
      images: [
        {
          image: require("@/assets/marquee/nodejs-marquee.svg"),
        },
        {
          image: require("@/assets/marquee/python-marquee.svg"),
        },
        {
          image: require("@/assets/marquee/git-scm-marquee.svg"),
        },
        {
          image: require("@/assets/marquee/linux-marquee.svg"),
        },
        {
          image: require("@/assets/marquee/django-logo-marquee.svg"),
        },
        {
          image: require("@/assets/marquee/vue-marquee.svg"),
        },
        {
          image: require("@/assets/marquee/javascript-logo-marquee.svg"),
        },
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.marquee {
  background: rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  height: 100%;
  overflow: hidden;

  & > ul {
    display: flex;
    gap: 20px;
    align-items: center;
    padding-left: 0;
    justify-content: center;

    & > li {
      list-style: none;
      display: flex;
      align-items: center;

      & > * {
        filter: grayscale(100%);
        transition: 2s;

        &:hover {
          filter: grayscale(0);
          transition: 2s;
        }
      }
    }
  }
}

@media screen and (max-width: 1142px) {
  ul {
    padding-left: 12px !important;
    justify-content: start !important;
  }
}
</style>
