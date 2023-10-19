<!-- 添加链路 -->
<template>
  <el-form :model="form" label-width="290px" ref="formRef" :rules="rules">
    <el-form-item label="请输入交换机名:" prop="switch">
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
import { ref } from 'vue'
const formRef = ref(null)
  // 数据源
const form = ref({
  switch: ''
})
// 确认事件
const handleConfirm = () => {
   // 表单统一验证
   formRef.value.validate((valid) => {
    if (valid) {
      console.log('submit!')
      console.log(form.value)
      ElMessageBox.confirm(
        '确定添加',
        'Warning',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
      .then(() => {
        axios({
            method: 'post',
            url: '/addswitch',
            data: { switch: form.value.switch }
          }).then(res => {
          // await addlink(form.value)
            ElMessage({
              message: '提交成功',
              type: 'success'
            })
          })
        })
      .catch(() => {
        ElMessage({
            type: 'info',
            message: '取消添加'
          })
      })
    } else {
      console.log('error submit!')
      return false
    }
  })
}
const rules = ref({
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
