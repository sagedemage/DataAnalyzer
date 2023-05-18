<script setup>
import { defineAsyncComponent } from 'vue'
</script>

<script>
/* UI Components */
const Navbar = defineAsyncComponent(() => import('@/components/ui/Navbar.vue'));
const Footer = defineAsyncComponent(() => import('@/components/ui/Footer.vue'));

/* Page Components */
const Home = defineAsyncComponent(() => import('@/components/pages/Home.vue'));
const About = defineAsyncComponent(() => import('@/components/pages/About.vue'));
const NotFound = defineAsyncComponent(() => import('@/components/pages/NotFound.vue'));
const Dashboard = defineAsyncComponent(() => import('@/components/pages/Dashboard.vue'));
const Login = defineAsyncComponent(() => import('@/components/pages/Login.vue'));
const Register = defineAsyncComponent(() => import('@/components/pages/Register.vue'));

const routes = {
  '/': Home,
  '/about': About,
  '/dashboard': Dashboard,
  '/login': Login,
  '/register': Register
}

export default {
  data() {
    return {
      currentPath: window.location.hash
    }
  },
  computed: {
    currentView() {
      return routes[this.currentPath.slice(1) || '/'] || NotFound
    }
  },
  mounted() {
    window.addEventListener('hashchange', () => {
          this.currentPath = window.location.hash
        })
  }
}
</script>

<template>
  <div id="body">
    <Navbar />
    <main>
      <component :is="currentView" />
    </main>
    <Footer id="footer" />
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
</style>
