<template>
    <div>
        <h1>聊天室</h1>
        <div class="login-form">
            <div class="avtar">
                <img src="../assets/login/images/avtar.png" />
            </div>
            <form>
                <input type="text" placeholder="Username" v-model="user.user_name" />

                <input type="password" placeholder="Password" v-model="user.user_pwd" />
            </form>
            <div class="signin">
                <input type="submit" value="Login" @click="login" />
            </div>
        </div>
    </div>
</template>

<script>
import store from "../store";

export default {
    data: function () {
        return {
            user: {
                user_name: "",
                user_pwd: "",
            },
        };
    },

    methods: {
        login() {
            store
                .dispatch("req", {
                    url: "login",
                    data: {
                        username: this.user_name,
                        user_pwd: this.user_pwd,
                    },
                })
                .then((rep) => console.log(rep));
        },
    },
};
</script>

<style>
@import "../assets/login/css/index.css";
</style>