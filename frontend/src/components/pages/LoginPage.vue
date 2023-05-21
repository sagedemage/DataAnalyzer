<script>

import Cookies from "universal-cookie";

export default {
    data: () => ({
        response_json: null,
        auth: null,
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

    methods: {
        async login() {
            /* Login POST request */
            const body = {username: this.username, password: this.password};

            const response = await fetch("http://localhost:8000/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                }, 
                body: JSON.stringify(body)
            });
            this.response_json = await response.json();
            if (this.response_json["auth"] === true) {
                const cookies = new Cookies();
                cookies.set("token", this.response_json["token"]);
                this.$router.push('/dashboard')
                
            }
            else {
                this.auth = false;
                this.err_msg = this.response_json["err_msg"]
            }
        }
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