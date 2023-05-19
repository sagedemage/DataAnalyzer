<script setup>
import { defineAsyncComponent } from "vue"
</script>

<script>
/* UI Components */
const NavbarUI = defineAsyncComponent(() => import("@/components/ui/NavbarUI.vue"));
const FooterUI = defineAsyncComponent(() => import("@/components/ui/FooterUI.vue"));

/* Page Components */
const HomePage = defineAsyncComponent(() => import("@/components/pages/HomePage.vue"));
const AboutPage = defineAsyncComponent(() => import("@/components/pages/AboutPage.vue"));
const PageNotFound = defineAsyncComponent(() => import("@/components/pages/PageNotFound.vue"));
const DashboardPage = defineAsyncComponent(() => import("@/components/pages/DashboardPage.vue"));
const LoginPage = defineAsyncComponent(() => import("@/components/pages/LoginPage.vue"));
const RegisterPage = defineAsyncComponent(() => import("@/components/pages/RegisterPage.vue"));

const routes = {
  "/": HomePage,
  "/about": AboutPage,
  "/dashboard": DashboardPage,
  "/login": LoginPage,
  "/register": RegisterPage
}

export default {
  data() {
    return {
      currentPath: window.location.hash
    }
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || "/"] || PageNotFound
    }
  },
  mounted() {
    window.addEventListener("hashchange", () => {
          this.currentPath = window.location.hash
        })
  }
}
</script>

<template>
  <div id="body">
    <NavbarUI />
    <main>
      <component :is="currentView" />
    </main>
    <FooterUI id="footer" />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}

.alert {
    padding-left: 20px;
    padding-right: 20px;
    padding-top: 10px;
    padding-bottom: 10px;
    border-radius: 5px;
}

.alert-error {
    background-color: #ffd5d5;
    color: darkred;
    border: #ffb7b7 1px solid;
}

.alert-success {
    background-color: #d6ffd5;
    color: darkgreen;
    border: #b1fcaf 1px solid;
}
</style>
