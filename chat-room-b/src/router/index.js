import Router from 'vue-router'
import Vue from 'vue'

Vue.use(Router)

const center_view = () => import("../views/center_view.vue")
const login_view = () => import("../views/login_view.vue")

const routes = [{
	path: '/',
	redirect: '/login'
}, {
	path: '/center',
	name: 'center_view',
	component: center_view
}, {
	path: '/login',
	name: 'login_view',
	component: login_view
}]

const router = new Router({
	mode: 'history',
	base: '/',
	routes
})

export default router