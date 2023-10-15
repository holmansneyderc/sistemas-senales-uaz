import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: 'convolucion-discreta',
        name: 'convolucion discreta',
        component: () => import(/* webpackChunkName: "convolucion" */ '@/views/Convolution.vue'),
      },
      {
        path: 'convolucion-continua-funciones',
        name: 'convolucion continua por funciones',
        component: () => import(/* webpackChunkName: "convolucion" */ '@/views/Convolution.vue'),
      },
      {
        path: 'convolucion-continua-criterios',
        name: 'convolucion continua por criterios de existencia',
        component: () => import(/* webpackChunkName: "convolucion" */ '@/views/Convolution.vue'),
      }
    ],
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/convolucion-discreta',
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
