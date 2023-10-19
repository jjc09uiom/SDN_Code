import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: '/',
    component: () => import('../layout'),
    redirect: '/daoru',
    children: [
      {
        path: 'daoru',
        name: 'daoru',
        component: () => import('@/views/daoru/index.vue')
      },
      {
        path: 'addflow',
        name: 'addflow',
        component: () => import('@/views/addflow/index.vue')
      },
      {
        path: 'addhost',
        name: 'addhost',
        component: () => import('@/views/addhost/index.vue')
      },
      {
        path: 'addlink',
        name: 'addlink',
        component: () => import('@/views/addlink/index.vue')
      },
      {
        path: 'addswitch',
        name: 'addswitch',
        component: () => import('@/views/addswitch/index.vue')
      },
      {
        path: 'balance',
        name: 'balance',
        component: () => import('@/views/balance/index.vue')
      },
      {
        path: 'delflow',
        name: 'delflow',
        component: () => import('@/views/delflow/index.vue')
      },
      {
        path: 'delhost',
        name: 'delhost',
        component: () => import('@/views/delhost/index.vue')
      },
      {
        path: 'dellink',
        name: 'dellink',
        component: () => import('@/views/dellink/index.vue')
      },
      {
        path: 'delswitch',
        name: 'delswitch',
        component: () => import('@/views/delswitch/index.vue')
      },
      {
        path: 'seepicture',
        name: 'seepicture',
        component: () => import('@/views/seepicture/index.vue')
      },
      {
        path: 'details/:id',
        name: 'details',
        component: () => import('@/views/seeswitch/details.vue'),
        prop: true
      },
      {
        path: 'seeswitch',
        name: 'seeswitch',
        component: () => import('@/views/seeswitch/index.vue')
      },
      {
        path: 'subflow',
        name: 'subflow',
        component: () => import('@/views/subflow/index.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
