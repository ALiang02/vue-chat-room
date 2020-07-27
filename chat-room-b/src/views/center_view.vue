<template>
    <div>
        <hello-world :name="this.$store.state.name"></hello-world>
    </div>
</template>

<script>
export default {
    data: function () {
        return {};
    },
    components: {
        "hello-world": () => import("../components/HelloWorld.vue"),
    },
};
</script>
