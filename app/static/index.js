import ComponentSearch from './vue_components/search.js'
import { asyncDebounce } from './modules/debounce.js'
import { getStores } from './modules/api.js'

let debouncedGetStores = asyncDebounce(getStores , 100);

new Vue({
  el: '#searchApp',
  components: {
    'component-search': ComponentSearch,
  },
  data: function() {
    return {
      searchText: "",
      stores: []
    }
  }, 
  methods: {
    async handleUpdateText(text) {
      Vue.set(this, 'stores', [])
      this.searchText = text;
      if(text && text.length > 1) {
        let stores = await debouncedGetStores(text, 3);
        stores.forEach((store, ind) => {
          Vue.set(this.stores, ind, store[1]);
        });
      }
    }
  },
  template: /*html*/`
    <div>
      <component-search 
        v-on:updateSearchText="handleUpdateText"
        :search-text="searchText"
        :stores="stores">
      </component-search>
    </div>
  `,
})