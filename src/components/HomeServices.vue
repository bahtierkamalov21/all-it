<template lang="pug">
div
  div(class="wrapper")
    section(class="services" id="services")
      v-container(class="py-16 px-4")
        v-col 
          v-row(class="justify-space-between align-center")
            h2(class="the-title font-weight-bold")
              | На чем мы
              br
              | специализируемся?
            font-awesome-icon(icon="fa-solid fa-circle-check" class="subtitle")
        home-services-swiper(class="my-16")
    home-services-view
</template>

<script>
import HomeServicesSwiper from "@/components/HomeServicesSwiper";
import HomeServicesView from "@/components/HomeServicesView";

export default {
  name: "HomeServices",
  components: { HomeServicesSwiper, HomeServicesView },
};
</script>

<style scoped lang="scss">
.wrapper {
  position: relative;
}

.the-title {
  color: #ffffff;
  line-height: calc(var(--index) * 2);
  font-size: calc(var(--index) * 2);
}

.subtitle {
  color: #ffffff;
  font-size: calc(var(--index) * 3.2);
}

.services {
  height: 100%;
  position: relative;
  background-color: #323232;
  overflow: hidden;
  background-image: url("../assets/images/services-background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  box-shadow: 0 0 24px 0 rgba(0, 0, 0, 0.4);
}
</style>
