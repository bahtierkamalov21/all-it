<template lang="pug">
svg(class="logo" width="72" height="72" viewBox="0 0 72 72" fill="none" xmlns="http://www.w3.org/2000/svg")
  rect(width="72" height="72" rx="12" fill="#FAFAFA")
  path(id="logo-text" d="M23.3652 56H17.8012V18.664H23.3652V56ZM58.0326 23.292H46.1766V56H40.6646V23.292H28.7566V18.664H58.0326V23.292Z" fill="black")
  path(id="logo-circle" d="M9 12C9 9.79086 10.7909 8 13 8C15.2091 8 17 9.79086 17 12C17 14.2091 15.2091 16 13 16C10.7909 16 9 14.2091 9 12Z" fill="black")
    mask(id="mask0_210_27" style="mask-type:alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="72" height="72")
      rect(width="72" height="72" rx="12" fill="#FAFAFA")
  g(mask="url(#mask0_210_27)" id="bottom-box")
    path(d="M-11 72.2853C11 58.6853 16.1667 70.2853 16 77.7853" stroke="#2196F3" stroke-width="18")
</template>

<script>
export default {
  name: "LogoItem",
  data() {
    return {
      colors: ["#2196F3", "black", "pink", "lime"],
      element: null,
    };
  },
  mounted() {
    this.element = document.getElementById("logo-circle");
    setInterval(() => {
      this.changeColors();
    }, 4000);
  },
  methods: {
    changeColors() {
      const index = Math.floor(Math.random() * this.colors.length);
      this.element.setAttribute("fill", this.colors[index]);
    },
  },
};
</script>

<style scoped lang="scss">
#logo-text {
  animation: 2s logo-text ease-in-out;
}

#bottom-box {
  animation: 2s bottom-box ease-in-out;
}

#logo-circle {
  transition: all 2s ease-in-out;
}

@keyframes logo-text {
  from {
    opacity: 0;
  }

  to {
    opacity: 1;
  }
}

@keyframes bottom-box {
  from {
    transform: translateX(-20px);
  }

  to {
    transform: translateX(0);
  }
}
</style>
