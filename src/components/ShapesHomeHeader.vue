<template lang="pug">
div(class="shapes" ref="shapes")
  div(v-if="!theme")
    img(v-for="images in images.light" :class="{'hover' : images.active}" class="image" :src="images.image" alt="shapes" :key="images.id")
  div(v-else)
    img(v-for="item in images.dark" :class="{'hover' : item.active}" class="image" :src="item.image" alt="shapes" :key="item.id")
</template>

<script>
import { mapState } from "vuex";

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
        dark: [
          {
            image: require("@/assets/shapes/shapes-dark.svg"),
            active: true,
          },
          {
            image: require("@/assets/shapes/shapes-dark-two.svg"),
            active: false,
          },
          {
            image: require("@/assets/shapes/shapes-dark-tree.svg"),
            active: false,
          },
          {
            image: require("@/assets/shapes/shapes-dark-four.svg"),
            active: false,
          },
        ],
      },
      index: 0,
    };
  },
  computed: {
    ...mapState(["theme"]),
  },
  mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((item) => {
        if (item.isIntersecting) {
          window.interval = setInterval(() => {
            if (this.theme) {
              this.changeImages(this.images.dark);
            } else {
              this.changeImages(this.images.light);
            }
          }, 2000);
        } else clearInterval(window.interval);
      });
    });

    observer.observe(this.$refs.shapes);
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

@media screen and (max-width: 1086px) {
  .image {
    width: 70vw;
  }
}
</style>
