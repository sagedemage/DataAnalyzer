<script>
import { ref } from "vue";
import Cookies from "universal-cookie";
import Redirect from "@/Redirect";
import axios from "axios";

export default {
    data: () => ({
        //auth: null,
        err_msg: "",
        username: "",
        usernameRules: [
            value => {
                if (value?.length >= 6) {
                    return true
                }

                return "Username must be at least 6 characters."
            },
        ],
        password: "",
        passwordRules: [
            value => {
                if (value?.length >= 8) {
                    return true
                }

                return "Password must be at least 3 characters."
            },
        ],
    }),

    setup() {
        let auth = ref(undefined);
        let err_msg = ref(undefined);
    
        async function login() {
            axios.post("http://localhost:8000/api/login", {
                username: this.username,
                password: this.password
            })
                .then(function (response) {
                    console.log(response);
                    console.log(response.data.err_msg)
                    if (response.data.auth === true) {
                        const cookies = new Cookies();
                        cookies.set("token", response.data.token);
                        Redirect("/dashboard");
                    }
                    else {
                        auth.value = false;
                        err_msg.value = response.data.err_msg;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }

        return { auth, login }
    },

    methods: {
        /*async login() {
            / Login POST request /

            axios.post("http://localhost:8000/api/login", {
                username: this.username,
                password: this.password
            })
                .then(function (response) {
                    console.log(response);
                    if (response.data.auth === true) {
                        const cookies = new Cookies();
                        cookies.set("token", response.data.token);
                        Redirect("/dashboard");
                    }
                    else {
                        auth.value = false;
                        this.err_msg = response.data.err_msg;
                    }
                })
                .catch(function (error) {
                    console.log(error);
                });
        }*/
    }
}
</script>

<template>
    <v-sheet width="300" class="mx-auto">
        <div class="alert alert-error" v-if="auth === false" role="alert">{{ err_msg }}</div>
        <h1>Login</h1>
        <br>
        <v-form fast-fail @submit.prevent>
            <v-text-field v-model="username" label="username" :rules="usernameRules"></v-text-field>
            <v-text-field v-model="password" label="password" type="password" :rules="passwordRules"></v-text-field>

            <v-btn type="submit" block class="mt-2" @click="login()">Submit</v-btn>
        </v-form>
    </v-sheet>
</template>