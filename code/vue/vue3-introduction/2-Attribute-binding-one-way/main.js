const app = Vue.createApp({
    data() {
        return {
            image: './assets/images/cat.jpg',
            description: 'beautiful cat',
            url: 'https://mihaicorciu.ro/',
            styleIsActive: 'color:green; font-weight: bold;',
            styleIsNotActive: 'color:red; font-weight: bold;',
            isActive: 'isActive',
            isNotActive: 'isNotActive',    
        }
    }
})
