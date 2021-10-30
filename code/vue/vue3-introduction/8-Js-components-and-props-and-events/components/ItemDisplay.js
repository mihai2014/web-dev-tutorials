app.component('item-display', {
    props: {
      message: {
        type: String,
        required: true
      }
    },
    template:
    /*html*/
    `
    <p>{{ message }}</p>
    <p>Click on list elements below</p>
    <p>Cats display</p>
    <div>
    <item-details :details="cats" @show-selection="updateSelection"></item-details>
    </div>
    <p>Dogs display</p>
    <div>
    <item-details :details="dogs" @show-selection="updateSelection"></item-details>
    </div>
    <p>{{ selections }}</p>
    <ul>
    <li v-for="item in selections">{{ item }}</li>
    </ul>
    `,
    data() {
        return {
            cats: ['ragdoll', 'british shorthair', 'persian'],
            dogs: ['beagle','bulldog','labrador'],
            selections: [],
        }
    },
    methods: {
      updateSelection(detail) {
        this.selections.push(detail)
      }
    }
})
  