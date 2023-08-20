const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: ["vuetify"],
  devServer: { allowedHosts: "all" },
  pwa: {
    name: "BMM Liter",
    themeColor: "#fff",
    msTileColor: "#000000",
    appleMobileWebAppCapable: "yes",
    appleMobileWebAppStatusBarStyle: "white",

    // настройки манифеста
    manifestOptions: {
      display: "landscape",
      background_color: "#fff",
      // ...другие настройки манифеста...
    },

    // настройка workbox-плагина
    workboxPluginMode: "InjectManifest",
    workboxOptions: {
      // swSrc необходимо в режиме InjectManifest
      swSrc: "dev/sw.js",
      // ...другие настройки Workbox...
    },
  },
});
