<template lang="pug">
div    
</template>

<script>
export default {
  name: "ProfileView",
  created() {
    this.determineWhetherUserAuthorized();
  },
  methods: {
    // Determine whether the user is authorized
    determineWhetherUserAuthorized() {
      if (!this.$store.state.user) {
        this.$router.push("/signin");
      } else null;
    },
  },
};
</script>
