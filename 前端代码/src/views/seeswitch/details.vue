<template :model="form">
  <el-row>
      <el-button type="primary" @click="goBack()" class="back">返回</el-button>
  </el-row>
  <!-- <el-row prop="dpid" v-model="form.dpid" style="margin:10px 50px">
      dpid:
  </el-row> -->
  <el-row prop="dpid" style="margin:10px 50px">
      dpid: {{ dpidflow }} 的流表
  </el-row>
  <el-space direction="vertical">
      <el-card
          v-for="(value,key,index) in tableData"
          :key="index"
          class="box-card"
          style="width: 700px;margin-left: 50px;">
          <template #header>
              <div class="card-header">
                  <span>第{{ index }}条流表</span>
              </div>
          </template>
          <div class="text item">
          {{ value }}
          </div>
      </el-card>
  </el-space>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import router from '@/router'
// import { getswitch } from '../../api/seeswitch'
const tableData = ref([])
const id = ref()
const dpidflow = ref()
// 得到用户数据
const initGetDetailsList = async () => {
  id.value = router.currentRoute.value.params.id
  console.log(id.value)
  axios({
    method: 'get',
    url: '/seeswitch'
  }).then(res => {
    // console.log(res)
    const dpid = res.data[id.value]
    dpidflow.value = dpid.dpid
    console.log(dpid)
    console.log(dpid.flow)
    // total.value = res.total
    tableData.value = dpid.flow
  }).catch(res => {
    console.log('fail')
  })
// id.value = router.currentRoute.value.params.id
// console.log(id.value)
// const res = await getswitch()
// const dpid = res.data.records[id.value - 1]
// console.log(dpid)
// console.log(dpid.flow)
// // total.value = res.total
// tableData.value = dpid.flow
}
initGetDetailsList()
// const handleDetail = () => {
//     router.replace('/details')
// }
// 返回
const goBack = () => {
router.replace('/seeswitch')
}
</script>

<style lang="scss" scoped>
.back{
  margin-left: 50px;
  margin-bottom: 20px;
}
</style>
