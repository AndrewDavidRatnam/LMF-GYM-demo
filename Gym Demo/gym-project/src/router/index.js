import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoadingPage from '../components/LoadingPage.vue'
import GymForm from '../components/GymForm.vue'

const router = createRouter({
  history: createWebHistory(),
 routes: [
  { path: '/', name: 'home', component: () => import('../views/HomeView.vue') },
  { path: '/loading', name: 'loading', component: () => import('../components/LoadingPage.vue') },
  { path: '/join', name: 'join', component: () => import('../components/GymForm.vue') }
]
})

export default router