<template lang="pug">
div
  section(class="forms py-16")
    v-container(class="px-6")
      h2(class="mb-4") Получить консультацию
      v-card(class="card" elevation="0" color="transparent")
        div(class="d-flex align-end")
          div(class="socials d-flex align-center")
            v-card(
              elevation="0"
              v-for="(item, index) in forms" 
              :key="item.name" 
              :class="item.name + ' d-flex align-center pa-2 pl-3 font-weight-bold ' + (item.active ? 'active' : null)"
            )
              font-awesome-icon(
                :icon="'fa-brands ' + item.icon"
                class="mr-2 right-icon"
              )
              | {{ item.title }}
          div(class="top-orange ml-6")
        v-card(elevation="0")
          //- home-forms-google(v-if="activeFormId === 0")
          home-forms-telegram(v-if="activeFormId === 1")
</template>

<script>
import HomeFormsGoogle from "./HomeFormsGoogle";
import HomeFormsTelegram from "./HomeFormsTelegram";

export default {
  name: "HomeForms",
  data() {
    return {
      activeFormId: 1,
      forms: [
        // {
        //   id: 0,
        //   title: "Google",
        //   name: "google",
        //   icon: "fa-google",
        //   active: false,
        // },
        {
          id: 1,
          title: "Telegram",
          name: "telegram",
          icon: "fa-telegram",
          active: true,
        },
      ],
    };
  },
  components: { HomeFormsGoogle, HomeFormsTelegram },
  mounted() {},
  methods: {
    setActiveForm(id) {
      this.forms.forEach((item) => {
        item.active = false;
      });
      this.forms[id].active = true;
      this.activeFormId = id;
    },
  },
};
</script>

<style scoped lang="scss">
.card {
  & > *:last-child {
    border-top-left-radius: 0 !important;
    border-top-right-radius: 24px !important;
    border-bottom-left-radius: 24px !important;
    border-bottom-right-radius: 24px !important;
    box-shadow: 10px 10px 24px 0 rgba(0, 0, 0, 0.15) !important;
    border: 2px solid #666;
  }
}

.top-orange {
  width: 40%;
  height: 24px;
  background-color: orange;
  border-top-left-radius: 12px;
  border-top-right-radius: 12px;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.15) inset,
    0 0 10px 0 rgba(0, 0, 0, 0.15);
  position: relative;

  &::before {
    content: "";

    position: absolute;
  }
}

.socials {
  gap: 4px;

  & > * {
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.15) !important;
    cursor: pointer;
    min-width: 200px;
    overflow: hidden;
    border-top-left-radius: 12px !important;
    border-top-right-radius: 12px !important;
    border-bottom-left-radius: 0px !important;
    border-bottom-right-radius: 0px !important;
    transition: all 0.5s ease-in-out;

    &.telegram:hover {
      transition: all 0.5s ease-in-out;
      background-color: var(--custom-blue);
      color: #fff;
    }
  }
}

.active {
  border: 2px solid #666;
  border-bottom: none;
}

@media screen and (max-width: 1086px) {
  .top-orange {
    width: 30%;
  }
}

@media screen and (max-width: 600px) {
  .socials {
    & > * {
      min-width: 142px;
    }
  }

  .top-orange {
    display: none;
  }
}
</style>
