export default {
  methods: {
    updateTitle(data) {
      if (data === this.$route.params.id) {
        const newString = data.toUpperCase() + data.slice(1);
        document.title = `ALL IT - ${newString}`;
      } else document.title = `ALL IT - ${data}`;
    },
  },
};
