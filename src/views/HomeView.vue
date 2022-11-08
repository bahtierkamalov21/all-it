<template lang="pug">
div
  button(@click="$router.push('/projects')")  
  div {{ $t("hello") }}
</template>

<script>
import updateTitle from "@/mixins/updateTitle";

export default {
  name: "HomeView",
  mixins: [updateTitle],
};
</script>
