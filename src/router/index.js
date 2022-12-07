import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProjectsView from "../views/ProjectsView.vue";
import ProjectsItemView from "../views/ProjectsItemView.vue";
import ProfileView from "../views/ProfileView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/projects",
    name: "projects",
    component: ProjectsView,
  },
  {
    path: "/projects/:id",
    component: ProjectsItemView,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
