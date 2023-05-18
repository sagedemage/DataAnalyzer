import { createApp } from "vue"
import App from "./App.vue"

// Vuetify
import { createVuetify } from "vuetify"
import { aliases, mdi } from "vuetify/iconsets/mdi"
import * as components from "vuetify/components"
import * as directives from "vuetify/directives"

import "./assets/main.css"

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

createApp(App).use(vuetify).mount("#app")
