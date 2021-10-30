const app = Vue.createApp({
    data() {
        return {
            selectedVariant: 0,
            selectedId: 0,
            selectedClass: '-',
            selectedImage: '-',
            variants: [
                { id: 1, animalClass: 'cat1', color: 'blue', image: './assets/images/cat1.jpg' },
                { id: 2, animalClass: 'cat2', color: 'blue', image: './assets/images/cat2.jpg' }, 
                { id: 3, animalClass: 'dog1', color: 'red', image: './assets/images/dog1.jpg' }, 
                { id: 4, animalClass: 'dog2', color: 'red', image: './assets/images/dog2.jpg' }, 
            ]    
        }
    },
    methods: {
        updateDisplay(index) {
            this.selectedVariant = index
        }
    },
    computed: {
        image() {
            return this.variants[this.selectedVariant].image
        },
        animalClass() {
            return this.variants[this.selectedVariant].animalClass
        }, 
        color() {
            return this.variants[this.selectedVariant].color
        },                       
    }
})
