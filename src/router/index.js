import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import ProjectsView from "../views/ProjectsView.vue";
import ProjectsItemView from "../views/ProjectsItemView.vue";
import ProfileView from "../views/ProfileView.vue";
import SigninView from "../views/SigninView.vue";
import SignupView from "../views/SignupView.vue";
import PageNotFound from "../views/PageNotFound.vue";
import RestorePassword from "../views/RestorePassword.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "*",
    component: PageNotFound,
  },
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/signin",
    name: "signin",
    component: SigninView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupView,
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
    children: [
      {
        name: "projectsCategory",
        path: "category/:slug",
      },
    ],
  },
  {
    path: "/projects/:slug",
    name: "project",
    component: ProjectsItemView,
  },
  {
    path: "/restore",
    name: "restore",
    component: RestorePassword,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
