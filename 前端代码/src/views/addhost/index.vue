<!-- 添加链路 -->
<template>
  <el-form :model="form" label-width="290px" ref="formRef" :rules="rules">
    <el-form-item label="请输入主机名:" prop="host">
          <el-input v-model="form.host" />
    </el-form-item>
    <el-form-item label="请输入IP:" prop="ip">
          <el-input v-model="form.ip" />
    </el-form-item>
    <el-form-item label="请输入默认连接的交换机: " prop="switch">
          <el-input v-model="form.switch" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleConfirm">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
// import { addhost } from '../../api/addhost'
import { ref } from 'vue'
const formRef = ref(null)
  // 数据源
const form = ref({
  host: '',
  switch: '',
  ip: ''
})
// 确认事件
const handleConfirm = () => {
   // 表单统一验证
   formRef.value.validate((valid) => {
    if (valid) {
      console.log('submit!')
      // form.value = JSON.stringify(form.value)
      console.log(form.value)
      ElMessageBox.confirm(
        '确定加入',
        'Warning',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
      .then(() => {
        // const path = 'http://192.168.216.128:5000/addhost'
          axios({
            method: 'post',
            url: '/addhost',
            data: { host: form.value.host, switch: form.value.switch, ip: form.value.ip }
          }).then(res => {
              // await addhost(form.value)
            ElMessage({
              message: '提交成功',
              type: 'success'
            })
          })
        })
      .catch(() => {
        ElMessage({
            type: 'info',
            message: '取消删除'
          })
      })
    } else {
      console.log('error submit!')
      return false
    }
  })
}
const rules = ref({
  host: [
    {
      required: true,
      message: '不能为空',
      trigger: 'blur'
    }
  ],
  ip: [
    {
      required: true,
      message: '不能为空',
      trigger: 'blur'
    }
  ],
  switch: [
    {
      required: true,
      message: '不能为空',
      trigger: 'blur'
    }
  ]
})
</script>

<style lang="scss" scoped>
.el-input{
  width: 50% !important;
}

</style>
