<template>
    <div>
        <div>{{name}}</div>
        <div>hello,world!</div>
        <el-button type="primary">主要按钮</el-button>
    </div>
</template>

<script>
export default {
    props: ["name"],
};
</script>