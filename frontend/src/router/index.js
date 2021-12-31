import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Job from "../views/Job.vue"; // 追加

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/job/:id", // 追加
    name: "job",
    component: Job,
    props: true
  }
];

const router = new VueRouter({
  mode: "history",
  base: __dirname,
  routes
});

export default router;