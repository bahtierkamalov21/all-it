<template lang="pug">
div
  button(@click="$router.push('/')")
</template>

<script>
import updateTitle from "@/mixins/updateTitle";

export default {
  name: "ProjectsView",
  mixins: [updateTitle],
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>
