import { createApp } from "vue"
import App from "./App.vue"
import { createRouter, createWebHashHistory } from "vue-router";

// Vuetify
import { createVuetify } from "vuetify"
import { aliases, mdi } from "vuetify/iconsets/mdi"
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"

import Cookies from "universal-cookie";

/* Page Components */
const HomePage = () => import("@/components/pages/HomePage.vue");
const AboutPage = () => import("@/components/pages/AboutPage.vue");
const PageNotFound = () => import("@/components/pages/PageNotFound.vue");
const DashboardPage = () => import("@/components/pages/DashboardPage.vue");
const LoginPage = () => import("@/components/pages/LoginPage.vue");
const RegisterPage = () => import("@/components/pages/RegisterPage.vue");

async function AuthRoute() {
  let is_authenticated = false;

  const cookies = new Cookies();
  const token = cookies.get("token");

  const body = { token: token };

  const response = await fetch("http://localhost:8000/api/get-decoded-token", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body)
  });
  const response_json = await response.json();
  is_authenticated = response_json["auth"];

  return is_authenticated;
}

const routes = [
  {
    path: "/",
    component: HomePage
  },
  {
    path: "/about",
    component: AboutPage
  },
  {
    path: "/dashboard",
    component: DashboardPage,
    beforeEnter: async(to, from) => {
      return await AuthRoute()
    }
  },
  {
    path: "/login",
    component: LoginPage
  },
  {
    path: "/register",
    component: RegisterPage
  },
  {
    path: "/:catchAll(.*)",
    component: PageNotFound
  }
]

const vuetify = createVuetify({
  components,
  directives,
  icon: {
    aliases,
    sets: {
      mdi,
    }
  },
})

const router = createRouter({
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})

const app = createApp(App)

app.use(vuetify)

app.use(router)

app.mount("#app")
