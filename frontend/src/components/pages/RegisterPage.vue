<script>
import Redirect from "@/Redirect";
import axios from "axios";

export default {
    data: () => ({
        registered: null,
        err_msg: "",
        email: "",
        emailRules: [
            value => {
                if (value === "") {
                    return "Field can't be empty."
                }
                else if (value?.length < 6) {
                    return "Email must be at least 6 characters."
                }
                return true
            },
        ],
        username: "",
        usernameRules: [
            value => {
                if (value === "") {
                    return "Field can't be empty."
                }
                else if (value?.length < 6) {
                    return "Username must be at least 6 characters."
                }
                return true
            },
        ],
        password: "",
        passwordRules: [
            value => {
                if (value === "") {
                    return "Field can't be empty."
                }
                else if (value?.length < 8) {
                    return "Password must be at least 8 characters."
                }
                else if (!/[0-9]/.test(value)) {
                    return "Password must contain a number"
                }
                return true
            },
        ],
        confirm: "",
        confirmRules: [
            value => {
                if (value?.length >= 8) {
                    return true
                }

                return "Password must be at least 6 characters."
            },
        ],
    }),

    methods: {
        async register() {
            /* Login POST request */

            axios.post("http://localhost:8000/api/register", {
                email: this.email,
                username: this.username,
                password: this.password
            })
                .then(function(response) {
                    console.log(response.data.registered);
                    if (response.data.registered === true) {
                        Redirect("/login");
                    }
                    else {
                        console.log(response.data.err_msg)
                        //this.registered = false;
                        //this.err_msg = response.data.err_msg;
                    }
                })
                .catch(function(error) {
                    console.log(error);
                });
        }
    }
}
</script>

<template>
    <v-sheet width="300" class="mx-auto">
        <div class="alert alert-error" v-if="registered === false" role="alert">{{ err_msg }}</div>
        <h1>Register</h1>
        <br>
        <v-form fast-fail @submit.prevent>
            <v-text-field v-model="email" label="email" type="email" :rules="emailRules"></v-text-field>
            <v-text-field v-model="username" label="username" :rules="usernameRules"></v-text-field>
            <v-text-field v-model="password" label="password" type="password" :rules="passwordRules"></v-text-field>
            <v-text-field v-model="confirm" label="confirm password" type="password" :rules="confirmRules"></v-text-field>
            <v-btn type="submit" block class="mt-2" @click="register()">Submit</v-btn>
        </v-form>
    </v-sheet>
</template>