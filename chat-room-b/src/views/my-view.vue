<template>
    <div>
        <hello-world :name="store.state.name"></hello-world>
    </div>
</template>

<script>
import store from "../store";

export default {
    data: function () {
        return {
            store,
        };
    },
    components: {
        "hello-world": () => import("../components/HelloWorld.vue"),
    },
};
</script>
