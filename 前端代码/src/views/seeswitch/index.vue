<template>
  <el-table
  :dialogTableVal="dialogTableVal"
  :data="tableData" stripe border style="width: 1100px;margin-left:50px;font-size: 17px" class="exporttable">
    <el-table-column
    v-for="(item, index) in options"
    :prop="item.prop"
    :key="index"
    label="dpid"
    :width="item.width"
    >
    <template #default="{ row }" v-if="item.prop === 'action'">
      <el-button
        type="primary"
        size="small"
        :icon="Edit"
        @click="handleDetail(row)"
      >查看详情</el-button>
    </template>
    </el-table-column>
  </el-table>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import router from '@/router'
// import { getswitch } from '@/api/seeswitch.js'
const options = [
  {
    label: 'dpid',
    prop: 'dpid',
    width: '800'
  },
  {
    label: '操作',
    prop: 'action',
    width: '300'
  }
]
const tableData = ref([])
const initGetSwitchList = async () => {
  axios({
    method: 'get',
    url: '/seeswitch'
  }).then(res => {
    console.log(res)
    // total.value = res.total
    tableData.value = res.data
    console.log(res.data)
  })
}
// const initGetSwitchList = async () => {
//   const res = await getswitch()
//     // console.log(res)
//     // total.value = res.total
//     tableData.value = res.data.records
//     console.log(tableData.value)
//     // console.log(res.data.records)
// }
initGetSwitchList()
const dialogTableVal = ref({})
const handleDetail = (row) => {
  console.log(row.id)
  router.push({ name: 'details', params: { id: row.id } })
}
</script>

<style lang="scss" scoped>
// .exporttable{
//   border: solid 1px #c0c0c0;
// }

</style>
