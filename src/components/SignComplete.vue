<template lang="pug">
div
  v-card(elevation="0" class="card d-flex justify-space-around align-center flex-column" min-height="320")
    v-icon(color="green") mdi-check-decagram
    v-card-text Через 5 секунд страница будет перезагружена
</template>

<script>
export default {
  name: "SignComplete",
};
</script>

<style scoped lang="scss">
.card {
  & > *:first-child {
    margin-top: 86px;
    margin-bottom: 56px;
    font-size: 82px !important;
  }
}
</style>
