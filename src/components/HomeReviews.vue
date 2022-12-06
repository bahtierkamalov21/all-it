<template lang="pug">
div
  section(class="reviews py-16")
    v-container(class="pt-10 px-6")
      v-col
        v-row(class="align-center")
          div(class="left")
            h2 Отзывы
          div(class="right")
</template>

<style scoped lang="scss">
.reviews {
  & > div {
    background-color: transparent !important;
  }
}

h2 {
  font-size: var(--section-title);
}
</style>
