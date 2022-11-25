<template lang="pug">
div
  marquee(class="marquee" behavior="scroll", direction="right" loop="-1") 
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
  background: rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  height: 100%;

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
