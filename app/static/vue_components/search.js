import Vue from "../vue.js"
import { getStores } from '../modules/api.js'

export default {
  data() {
    return {
      searchedStores: []
    }
  },
  props: {
    searchText: {
      type: String,
      required: false
    },
    stores: {
      type: Array,
      required: false
    }
  },
  methods: {
    updateSearchText(text) {
      this.$emit('updateSearchText', text);
    },
    async loadAllStores() {
      // there are many ways to optimize this ugly 999
      let newStores = await getStores(this.searchText, 999, this.stores.length);
      const starting_index = this.searchedStores.length;
      newStores.forEach((store, ind) => {
        Vue.set(this.searchedStores, starting_index + ind, store[1]);
      })
    },
    showResult() {
      Vue.set(this, 'searchedStores', [...this.stores]);
      const trigger = document.getElementById('trigger');
      const container = document.getElementById('container');
      const opt = {root: container, threshold: 0};
      let observer = new IntersectionObserver((entries, self) => {
        entries.forEach(entry => {
          if (entry.isIntersecting && this.stores.length > 2) {
            this.loadAllStores();
            self.unobserve(entry.target);
          }
        });
      }, opt);
      observer.observe(trigger);
    }
  },
  // I have a syntax highlighter for this!
  template: /*html*/`
    <div>
      <h1>Search App</h1>
      <label for="storeSearch">Find a store:</label>
      <input 
        type="text"
        list="stores"
        :value="searchText"
        v-on:input="updateSearchText($event.target.value)"
      />
      <button 
        type="button"
        :style="{cursor: stores.length > 0 ? 'pointer' : 'auto'}"
        :disabled="stores.length == 0"
        v-on:click="showResult()">Show results</button>
      <datalist v-if="stores.length > 0" id="stores">
        <! –– datalist automatically excludes results that do not match the string ––>
        <! –– the only way to display results that come from postocodes ––>
        <! –– is to add the searched string itslef as value ––>
        <option v-for="(store, ind) in stores" :key="'store' + ind" :value="searchText">{{store}}</option>
      </datalist>
      <div id="container">
        <div id="scr">
          <div
            v-for="(sStore, ind) of searchedStores"
            :key="'s_' + ind + sStore"
            class="store">
            {{sStore}}
          </div>
          <div id="trigger"></div>
        </div>
      </div>
    </div>
  `,
}
