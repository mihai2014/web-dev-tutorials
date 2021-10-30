const app = Vue.createApp({
    data() {
        return {
            flag: true,
            animals: ['cat', 'dog', 'dove', 'bear'],
            numbers: ['1', '2', '3', '4'],
            variants: [
              { id: 2234, color: 'green' },
              { id: 2235, color: 'blue' },
            ]
        }
    }
})
