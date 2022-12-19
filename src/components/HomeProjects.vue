<template lang="pug">
div
  section(class="projects")
    v-container(class="container my-16")
</template>

<script>
export default {
  name: "HomeProjects",
};
</script>

<style scoped lang="scss">
.projects {
  background-color: #212121;
  background-image: url("../assets/images/about-background.png");
  background-attachment: fixed;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: bottom;
  position: relative;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container {
  height: 80vh;
  backdrop-filter: blur(6px);
  border-radius: 20px;
  box-shadow: var(--shadow-2xl);
}
</style>
