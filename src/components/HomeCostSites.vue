<template lang="pug">
section(class="cost-sites py-16" id="cost-sites")
  v-container(class="px-4")
   h2(class="font-weight-bold white--text mb-6") Стоимость сайтов
   home-cost-sites-card
</template>

<script>
import HomeCostSitesCard from "./HomeCostSitesCard";

export default {
  name: "HomeCostSites",
  components: { HomeCostSitesCard },
};
</script>

<style scoped lang="scss">
.cost-sites {
  background-color: #323232;
  overflow: hidden;
  background-image: url("../assets/images/services-background.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  box-shadow: 0 0 24px 0 rgba(0, 0, 0, 0.4);
}
</style>
