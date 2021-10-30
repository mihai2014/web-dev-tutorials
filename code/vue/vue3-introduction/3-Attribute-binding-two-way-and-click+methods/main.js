const app = Vue.createApp({
    data() {
        return {
            firstName: 'John',
            lastName: 'Doe',
        }
    },
    methods: {
        reset(data) {
            this.firstName = 'John';
            this.lastName = 'Doe';
        }
    },
});
