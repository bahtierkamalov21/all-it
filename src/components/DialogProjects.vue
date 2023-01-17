<template lang="pug">
div
    v-dialog(v-model="dialogProjects")
</template>

<script>
export default {
  name: "DilaogProjects",
  props: {
    dialogProjects: Boolean,
  },
  watch: {
    dialogReviews() {
      this.sendDialogProjects();
    },
  },
  methods: {
    sendDialogProjects() {
      this.$emit("getDialogProjects", this.dialogProjects);
    },
  },
};
</script>

<style scoped lang="scss"></style>
