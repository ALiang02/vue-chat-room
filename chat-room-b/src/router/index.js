import Router from 'vue-router'
import Vue from 'vue'

Vue.use(Router)

const myView = () => import('../views/login-page.vue')

const routes = [{
	path: '/',
	name: 'myView',
	component: myView
}]

const router = new Router({
	mode: 'hash',
	base: '/',
	routes
})

export default router