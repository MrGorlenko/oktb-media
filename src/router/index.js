import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import News from '@/views/News'
import News_item from '@/views/News_item'
import Leaders from '@/views/Leaders'
import NewsArticle from '@/components/NewsArticle'
import _NewsArtic from '@/components/_NewsArtic'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/News',
    name: 'News',
    component: News 
  },
  {
    path: '/NewsArticle',
    name: 'NewsArticle',
    component: NewsArticle,
    //props:true
  },
  {
    path: '/_NewsArtic/:id',
    name: 'NewsArtic',
    component: _NewsArtic,
    //props:true
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/News_item',
    name:'News_item',
    component: News_item
  },
  {
    path: '/Leaders',
    name: 'Leaders',
    component: Leaders
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
