<template lang="pug">
div
  div(class="d-flex align-center justify-center flex-column" style="min-height: 420px;")
    v-progress-circular(:size="100" width="6" color="primary" indeterminate)
    v-card-text(class="text-center pb-0") Загрузка...
</template>

<script>
export default {
  name: "LoadingItem",
};
</script>
