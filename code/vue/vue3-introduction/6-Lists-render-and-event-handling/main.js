const app = Vue.createApp({
    data() {
        return {
            selectedId: 0,
            selectedClass: '-',
            selectedImage: '-',
            variants: [
                { id: 1, class: 'cat1', image: './assets/images/cat1.jpg' },
                { id: 2, class: 'cat2', image: './assets/images/cat2.jpg' }, 
                { id: 3, class: 'dog1', image: './assets/images/dog1.jpg' }, 
                { id: 4, class: 'dog2', image: './assets/images/dog2.jpg' }, 
            ]    
        }
    },
    methods: {
        updateDisplay(variant) {
            this.selectedId = variant.id;
            this.variants.forEach(element => {
                if(element.id == variant.id) {
                    this.selectedClass = element.class;
                    this.selectedImage = element.image;
                }
            });
        }
    }
})
