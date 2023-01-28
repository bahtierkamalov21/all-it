<template lang="pug">
div
  div(class="faq" id="support")
    v-container(class="pt-16 pb-12 px-6 container")
      div(class="mb-2 header")
        h2(class="black--text") {{ escaped }}
      v-col
        v-row(class="align-start justify-space-between")
          div(class="left mb-2")
            v-list
              v-list-group(
                v-for="item in listFaq"
                :key="item.id"
                style="background-color: var(--v-background-base);"
                class="d-inline-block mr-4 mb-4 group rounded-lg"
                :value="false"
              )
                template(v-slot:activator)
                  v-list-item-title(class="list-title")
                    | {{ item.title }}
                v-list-item-content
                  ul
                    li(v-for="li in item.list" :key="li.id")
                      | {{ li.text }}
          div(class="right")
            div(class="right-title font-weight-bold mb-2") Нет ответа на ваш вопрос?
            v-btn(
              class="text-capitalize font-weight-bold white--text"
              x-large
              rounded
              color="costumBlue" 
              elevation="0"
            )
              font-awesome-icon(
                icon="fa-brands fa-telegram"
                class="mr-2 right-icon"
              )
              div(class="ma-0")
                | Задайте 
                span(class="text-lowercase") вопрос в 
                | Telegram
  div(class="footer-bottom text-center font-weight-bold white--text pa-4")
    | © 2023 — 2023 BMM LITER - IT Разработка современных проектов
</template>

<script>
export default {
  name: "TheFaq",
  data() {
    return {
      escaped: "FAQ & ЧАВО",
      listFaq: [
        {
          title: "Сколько у нас стоит час?",
          list: [
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
          ],
        },
        {
          title: "Сколько у нас стоит час?",
          list: [
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
          ],
        },
        {
          title: "Сколько у нас стоит час?",
          list: [
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
          ],
        },
        {
          title: "Сколько у нас стоит час?",
          list: [
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
          ],
        },
        {
          title: "Сколько у нас стоит час?",
          list: [
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
            {
              text: "от 20 до 50$, в зависимости от вашей задачи и проекта.",
            },
          ],
        },
      ],
    };
  },
};
</script>

<style scoped lang="scss">
.faq {
  overflow: hidden;
  background-color: #ffffff;
  box-shadow: 0 0 24px 0 rgba(0, 0, 0, 0.2);
}

.container {
  height: 100%;
}

ul {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.left {
  width: 60%;
}

.footer-bottom {
  background-color: #212121;
  box-shadow: 0 -5px 10px 0 rgba(0, 0, 0, 0.2);
}

.group {
  background-color: rgba(0, 0, 0, 0.05);
  width: 46%;
}

.list-title {
  font-weight: 600;
  font-size: 16px;
  line-height: 20px;
}

.right {
  &-title {
    font-size: 1.75rem;
    color: #000000;
  }

  &-icon {
    font-size: 20px !important;
  }
}

@media screen and (max-width: 1142px) {
  .footer-bottom {
    margin-bottom: 58px;
  }

  .right {
    &-title {
      font-size: 1.5rem;
    }
  }

  .left {
    width: 100% !important;
  }
}

@media screen and (max-width: 600px) {
  .group {
    width: 100% !important;
  }

  .container {
    padding-top: 48px !important;
  }

  .right {
    &-title {
      font-size: calc(var(--index) * 1.8);
    }

    & > *:last-child {
      font-size: 14px !important;
    }
  }
}
</style>
