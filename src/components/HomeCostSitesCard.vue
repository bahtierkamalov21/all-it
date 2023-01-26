<template lang="pug">
div
  div(class="d-flex flex-wrap justify-center mx-auto container")
    div(class="card px-4 text-center" id="first")
      img(style="width: 80px; height: 80px;" class="mx-auto" src="@/assets/icons/icon-placeholder.svg" alt="icon")
      div(class="font-weight-bold title text-capitalize") landing page
      div(class="subtitle") Одностраничный сайт, обычно
        br
        | направленный на презентаию
        br 
        | конкретного продукта или проекта
      div(class="price text-capitalize font-weight-bold") от 14000 ₽
    div(class="card px-4 text-center" id="two")
      img(style="width: 80px; height: 80px;" class="mx-auto" src="@/assets/icons/icon-placeholder.svg" alt="icon")
      div(class="font-weight-bold title text-capitalize") многостраничник
      div(class="subtitle") Сайт, имеющий множество
        br 
        | дочерних страниц, подходи для
        br 
        | многих типов бизнеса 
      div(class="price text-capitalize font-weight-bold") от 26000 ₽
    div(class="card px-4 text-center" id="tree")
      img(style="width: 80px; height: 80px;" class="mx-auto" src="@/assets/icons/icon-placeholder.svg" alt="icon")
      div(class="font-weight-bold title text-capitalize") инернет-магазин
      div(class="subtitle") Сайт, имеющий возможность
        br
        | покупки товаров онлайн
      div(class="price text-capitalize font-weight-bold") от 33000 ₽
</template>

<script>
export default {
  name: "HomeCostSitesCard",
};
</script>

<style scoped lang="scss">
.container {
  gap: 26px;
}

.title {
  font-size: 24px;
  color: #fff;
}

.card {
  background: #0c2144;
  box-shadow: var(--shadow-lg) !important;
  display: flex;
  padding-top: 46px;
  padding-bottom: 26px;
  flex-direction: column;
  gap: 24px;
  border: 2px solid transparent;
  position: relative;
  border-radius: 16px;
  height: 350px;
  transition: 0.2s ease-in-out all;
  width: 350px;

  &:hover {
    transition: 0.2s ease-in-out all;
    background: #002b72;
    border: 2px solid #fff !important;
  }
}

.price {
  position: absolute;
  bottom: 26px;
  left: 50%;
  color: #fff;
  margin-right: -50%;
  transform: translate(-50%, 0);
  font-size: 18px;
}

.subtitle {
  color: #adb9c7;
  font-size: 14px;
}
</style>
