const app = Vue.createApp({
    data() {
        return {
            contor: 0,
        }
    },
    methods: {
        increment() {
            this.contor += 1;
        },
        decrement() {
            this.contor -= 1;
        }
    }
});
