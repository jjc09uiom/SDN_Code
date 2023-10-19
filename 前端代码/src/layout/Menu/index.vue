<template>
  <el-menu
    active-text-color="#ffd04b"
    :background-color="variables.menuBg"
    class="el-menu-vertical-demo"
    :default-active="defaultActive"
    text-color="#fff"
    router
    unique-opened
    :collapse="!$store.getters.siderType"
  >
    <el-menu-item
      :index="'/'+item.path"
      v-for="item in menusList"
      :key="item.path"
      @click="savePath(item.path)"
    >
      <template #title>
        <span>{{ item.name }}</span>
      </template>
    </el-menu-item>
    <el-sub-menu
    index="/build"
    key="build"
    @click="savePath('build')"
    >
    <template #title>
        <span>建立拓扑</span>
      </template>
      <el-menu-item
        :index="'/' + it.path"
        v-for="it in buildlist"
        :key="it.path"
        @click="savePath(it.path)"
      >
        <template #title>
          <span>{{ it.name }}</span>
        </template>
      </el-menu-item>
    </el-sub-menu>

  </el-menu>
</template>

<script setup>
// import { menuList } from '@/api/menu'
import { ref } from 'vue'
import variables from '@/styles/variables.scss'

// const iconList = ref(['user', 'setting', 'shop', 'tickets', 'pie-chart'])
// const icon = ref('menu')

const defaultActive = ref(sessionStorage.getItem('path') || '/daoru')
const menusList = ref([
  {
    path: 'daoru',
    name: '导入默认拓扑'
  },
  {
    path: 'addhost',
    name: '添加主机'
  },
  {
    path: 'addswitch',
    name: '添加交换机'
  },
  {
    path: 'addlink',
    name: '添加链路'
  },
  {
    path: 'dellink',
    name: '删除链路'
  },
  {
    path: 'delhost',
    name: '删除主机'
  },
  {
    path: 'delswitch',
    name: '删除交换机'
  }
])
const buildlist = ref([
      {
        path: 'seepicture',
        name: '查看当前拓扑'
      },
      {
        path: 'seeswitch',
        name: '查看拓扑中交换机与流表'
      },
      {
        path: 'addflow',
        name: '添加流表'
      },
      {
        path: 'subflow',
        name: '以文件的形式提交流表'
      },
      {
        path: 'delflow',
        name: '删除指定交互机的所有流表'
      }
])
// const initMenusList = async () => {
//   menusList.value = await menuList()
// }
// initMenusList()
const savePath = (path) => {
  sessionStorage.setItem('path', `/${path}`)
}
</script>

<style lang="scss" scoped>
.el-menu{
  --el-menu-item-height:50px;
}
</style>
