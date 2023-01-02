<template lang="pug">
div
  v-col 
    v-row 
      div(class="left rounded-xl pa-12")
      div(class="right d-flex align-center justify-center")
        font-awesome-icon(
          icon="fa-brands fa-google"
          class="right-icon"
        )
</template>

<script>
export default {
  name: "HomeFormsGoogle",
};
</script>

<style scoped lang="scss">
.right {
  width: 50%;
  position: relative;

  &-icon {
    font-size: calc(var(--section-title) * 3);
  }
}
</style>
