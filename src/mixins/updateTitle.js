export default {
  created() {
    if (this.$route.params.id) {
      const newString =
        this.$route.params.id[0].toUpperCase() + this.$route.params.id.slice(1);
      document.title = `ALL IT - ${newString}`;
    } else {
      switch (this.$route.path) {
        case "/":
          document.title = "ALL IT - Главная";
          break;
        case "/projects":
          document.title = "ALL IT - Проекты";
          break;
      }
    }
  },
};
