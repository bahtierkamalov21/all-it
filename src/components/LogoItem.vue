<template lang="pug">
div(class="logo")
  v-img(src="@/assets/logo.svg")
</template>

<script>
export default {
  name: "LogoItem",
};
</script>

<style scoped lang="scss">
.logo {
  width: 24px;
  height: 24px;
}
</style>
