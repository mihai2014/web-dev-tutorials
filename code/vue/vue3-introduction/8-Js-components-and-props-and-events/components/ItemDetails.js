app.component('item-details', {
    props: {
      details: {
        type: Array,
        required: true
      }
    },
    template:
    /*html*/
    `
    <ul>
      <li v-for="detail in details" @click="sendSelection(detail)">{{ detail }}</li>
    </ul>
    `,
    methods: {
      sendSelection(detail) {
        this.$emit('show-selection',detail)
      }
    }
  })
  