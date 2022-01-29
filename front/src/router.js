import Vue from 'vue'
import Router from 'vue-router'

import Index from './views/Index'
import Rules from './views/Rules'
import Signup from './views/Signup'
import Listing from './views/Listing'
import NotFound from './views/NotFound'
import Teams from './views/Teams'

Vue.use(Router)

const staticRoutes = [
  {
    path: '/',
    name: 'index',
    component: Index,
    meta: {
      title: 'Accueil',
      icon: 'home'
    }
  },
  {
    path: '/reglement',
    name: 'reglement',
    component: Rules,
    meta: {
      title: 'Règlement',
      icon: 'assignment'
    }
  },
  {
    path: '/inscription',
    name: 'inscription',
    component: Signup,
    meta: {
      title: 'Inscription',
      icon: 'edit'
    }
  },
  {
    path: '/listing',
    name: 'listing',
    component: Listing,
    meta: {
      title: "Liste d'inscrits",
      icon: 'list'
    }
  },
  {
    path: '/teams',
    name: 'teams',
    component: Teams,
    meta: {
      title: 'Teams',
      icon: 'people'
    }
  }
]

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    ...staticRoutes,
    {
      path: '*',
      component: NotFound
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { x: 0, y: 0 }
  }
})

export {
  staticRoutes,
  router
}
