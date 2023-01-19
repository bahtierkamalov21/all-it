<template lang="pug">
div
  v-dialog(v-model="dialogProjectsLocal" hide-overlay)
</template>

<script>
export default {
  name: "DilaogProjects",
  props: {
    dialogProjects: Boolean,
  },
  computed: {
    dialogProjectsLocal: {
      get() {
        return this.dialogProjects;
      },
      set(value) {
        this.$emit("getDialogProjects", value);
      },
    },
  },
};
</script>

<style scoped lang="scss"></style>
