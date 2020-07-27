<template>
    <div>
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
            this.$store
                .dispatch("req", {
                    url: "login",
                    data: this.user,
                })
                .then((rep) => {
                    if (rep.data["flag"] === 0) {
                        this.$router.push("/center");
                    } else {
                        alert("账号或密码错误");
                    }
                });
        },
    },
};
</script>

<style>
@import "../assets/login/css/index.css";
</style>