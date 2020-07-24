<template>
    <!-- <el-card>
        <div>
            <h2>聊天室</h2>
        </div>
        <div class="container">
            <label for="user_name">用户名：</label>
            <input
                id="user_name"
                name="user_name"
                type="text"
                placeholder="用户名"
                v-model="user.user_name"
            />
        </div>
        <div class="container">
            <label for="user_pwd">密码：</label>
            <input
                id="user_pwd"
                name="user_pwd"
                type="password"
                placeholder="密码"
                v-model="user.user_pwd"
            />
        </div>
        <div>
            <button id="btn_login" @click="login">登录</button>
        </div>
    </el-card>-->
    <div>
        <h1>聊天室</h1>
        <div class="login-form">
            <!-- <div class="close"></div> -->
            <!-- <div class="head-info">
                <label class="lbl-1"></label>
                <label class="lbl-2"></label>
                <label class="lbl-3"></label>
            </div>-->
            <!-- <div class="clear"></div> -->
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
        login() {},
    },
};
</script>

<style>
@import "../assets/login/css/index.css";
</style>