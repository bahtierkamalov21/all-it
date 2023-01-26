<template lang="pug">
div
  div(class="wrapper")
    section(class="services" id="services")
      v-container(class="py-16 px-6")
        v-col 
          v-row(class="justify-space-between align-center")
            h2(class="font-weight-bold white--text")
              | На чем мы
              br
              | специализируемся?
        home-services-swiper(class="my-8")
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

@media screen and (max-width: 768px) {
  .services {
    & > div {
      padding-bottom: 74px !important;
    }
  }
}

@media screen and (max-width: 600px) {
  .services {
    & > div {
      padding-bottom: 104px !important;
    }
  }
}
</style>
