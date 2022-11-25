<template lang="pug">
div
  div(v-if="!this.$vuetify.theme.dark")
    img(v-for="images in images.light" :class="{'hover' : images.active}" class="image" :src="images.image" alt="shapes")
</template>

<script>
export default {
  name: "ShapesHomeHeader",
  data() {
    return {
      images: {
        light: [
          {
            image: require("@/assets/shapes/shapes-light.svg"),
            active: true,
          },
          {
            image: require("@/assets/shapes/shapes-light-two.svg"),
            active: false,
          },
          {
            image: require("@/assets/shapes/shapes-light-tree.svg"),
            active: false,
          },
        ],
      },
      index: 0,
      show: true,
    };
  },
  mounted() {
    this.element = document.querySelector(".image");
    window.interval = setInterval(() => {
      if (this.$vuetify.theme.dark) {
        this.changeImages(this.images.dark);
      } else {
        this.changeImages(this.images.light);
      }
    }, 4000);
  },
  methods: {
    changeImages(data) {
      if (this.index === data.length - 1) {
        this.index = 0;
        data.forEach((item) => {
          item.active = false;
        });
        data[0].active = true;
      } else {
        this.index++;
        data.forEach((item, index) => {
          if (this.index === index) {
            item.active = true;
          } else item.active = false;
        });
      }
    },
  },
};
</script>

<style scoped lang="scss">
.image {
  position: absolute;
  right: -62px;
  bottom: -32px;
  opacity: 0;
  width: 50vw;
  transition: all 0.5s ease-in-out;
}

.hover {
  opacity: 1;
  transition: all 0.5s ease-in-out;
}
</style>
