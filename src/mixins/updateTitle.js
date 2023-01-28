export default {
  methods: {
    updateTitle(data) {
      if (data === this.$route.params.id) {
        const newString = data.toUpperCase() + data.slice(1);
        document.title = `BMM - ${newString}`;
      } else document.title = `BMM - ${data}`;
    },
  },
};
