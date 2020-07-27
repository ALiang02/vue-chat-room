import Vuex from 'vuex'
import Vue from 'vue'
import req from '../utils/request'
Vue.use(Vuex)

const store = new Vuex.Store({
	state: {
		name: 'jl'
	},
	actions: {
		req(store, url, data) {
			return req(url, data)
		}
	}
})

export default store