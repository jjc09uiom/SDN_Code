<!-- 删除链路 -->
<template>
  <el-form :model="form" label-width="290px" ref="formRef" :rules="rules">
    <el-form-item label="请输入要删除的主机（交换机）名：" prop="host1">
          <el-input v-model="form.host1" />
    </el-form-item>
    <el-form-item label="请输入要与其删除的主机（交换机）名：" prop="host2">
          <el-input v-model="form.host2" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleConfirm">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script  setup>
import { ElMessage, ElMessageBox } from 'element-plus'
import axios from 'axios'
import { ref } from 'vue'
const formRef = ref(null)
  // 数据源
const form = ref({
  host1: '',
  host2: ''
})
// 确认事件
const handleConfirm = () => {
    // 表单统一验证
  formRef.value.validate((valid) => {
    if (valid) {
      console.log('submit!')
      console.log(form.value)
      ElMessageBox.confirm(
        '确定删除',
        'Warning',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
      .then(() => {
        axios({
            method: 'post',
            url: '/dellink',
            data: { host1: form.value.host1, host2: form.value.host2 }
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
  host1: [
    {
      required: true,
      message: '不能为空',
      trigger: 'blur'
    }
  ],
  host2: [
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
