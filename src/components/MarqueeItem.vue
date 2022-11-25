<template lang="pug">
div
  marquee(class="marquee" behavior="alternate", direction="right") 
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
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.marquee {
  position: absolute;
  bottom: 32px;
  left: 32px;

  & > ul {
    display: flex;
    gap: 20px;
    align-items: center;

    & > li {
      list-style: none;
    }
  }
}
</style>
