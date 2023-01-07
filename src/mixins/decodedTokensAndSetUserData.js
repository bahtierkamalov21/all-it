import axios from "axios";

export default {
  methods: {
    decodedTokensAndSetUserData() {
      axios
        .get(this.$store.state.api_url + "decoded_tokens/", {
          params: {
            token: this.$store.state.token_access,
          },
          headers: {
            Authorization: `Bearer ${this.$store.state.token_access}`,
          },
        })
        .then((response) => {
          localStorage.setItem("decoded", response.data);
          this.$store.commit("setDecoded", response.data);

          // Получаем данные пользователя
          axios
            .get(
              this.$store.state.api_url +
                `users/${this.$store.state.decoded.user_id}/`
            )
            .then((response) => {
              // Сохраняем данные пользователя в store и localStorage
              localStorage.setItem("user", JSON.stringify(response.data));
              this.$store.commit("setUser", JSON.stringify(response.data));
              // Отображаем check template
              this.complete = true;
              // Перезагружаем страницу
              setTimeout(() => {
                location.reload();
              }, 4000);
            })
            .catch((errors) => {
              console.log(errors);
            });
        })
        .catch((errors) => {
          console.log(errors);
        });
    },
  },
};
