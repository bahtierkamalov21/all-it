<template lang="pug">
div
  div(class="marquee") 
    ul
      li(v-for="item in images" :key="item.id")
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

  & > ul {
    display: flex;
    gap: 20px;
    align-items: center;

    & > li {
      list-style: none;

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
</style>
