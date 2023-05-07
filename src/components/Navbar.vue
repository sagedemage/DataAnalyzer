<script setup>
defineProps({
  msg: {
    type: String,
    required: false
  }
})
</script>

<script>
  export default {
    data: () => ({
      drawer: false,
      group: null,
      items: [
        {
          title: 'Home',
          route: '#/',
        },
        {
          title: 'About',
          route: "#/about",
        },
        {
          title: 'Dashboard',
          route: "#/dashboard",
        },
        {
          title: 'Login',
          route: "#/login",
        },
        {
          title: 'Register',
          route: "#/register",
        }
      ],
    }),

    watch: {
      group () {
        this.drawer = false
      },
    },

    methods: {
	  navigate(route) {
      location.href = route;
      this.drawer = false;
  	}
	}
  }
</script>

<template>
  <div>
    <v-layout>
      <v-app-bar color="#2E8B57" prominent>
      <v-app-bar-nav-icon variant="text" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Learn Vue</v-toolbar-title>
        <v-spacer></v-spacer>
      </v-app-bar>
      <v-navigation-drawer v-model="drawer" location="left" temporary>
        <v-list flat dense nav class="py-1">
            <v-list-item-group color='primary' mandatory>
                <v-list-item
                    v-for="item in items"
                    :key="item.title"
                    dense
                    @click="navigate(item.route)"
                >
                    <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-title>{{ item.title }}</v-list-title>
                    </v-list-item-content>

                </v-list-item>
            </v-list-item-group>
        </v-list>
      </v-navigation-drawer>
    </v-layout>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}

.navbar {
  background-color: rgb(69, 69, 69);
  color: white;
}

</style>
