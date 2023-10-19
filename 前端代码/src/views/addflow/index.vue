<template>
    <!-- <div>添加流表</div> -->
    <!-- <div class="text-area">
      <el-input v-model="textarea" :rows="20" type="textarea" ref="textareaRef" placeholder="请以JSON格式输入流表"/>
      <el-button type="primary" @click="handleConfirm">提交</el-button>
    </div> -->
    <el-form :model="textarea" ref="textareaRef">
    <el-form-item>
          <!-- <el-input v-model="form.name1" /> -->
          <el-input v-model="textarea" :rows="20" type="textarea" placeholder="请以JSON格式输入流表"/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="handleConfirm">提交</el-button>
    </el-form-item>
  </el-form>
    </template>
<script setup>
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
// import { addflow } from '../../api/addflow'
import { ref } from 'vue'
const textareaRef = ref(null)
  // 数据源
const textarea = ref()
// 确认事件
const handleConfirm = () => {
   // 表单统一验证
   textareaRef.value.validate((valid) => {
    if (valid) {
      console.log('submit!')
      console.log(textarea.value)
      ElMessageBox.confirm(
        '确定提交',
        'Warning',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
      .then(() => {
          // await addflow(textarea.value)
          axios({
            method: 'post',
            url: '/addflow',
            data: { text: textarea.value }
          }).then(res => {
            console.log(1234)
            ElMessage({
              message: '提交成功',
              type: 'success'
            })
          })
        })
      .catch(() => {
        ElMessage({
            type: 'info',
            message: '取消提交'
          })
      })
    } else {
      console.log('error submit!')
      return false
    }
  })
}
</script>
<style lang="scss" scoped>
  .text-area textarea {
    width: 50%;
    height: 50%;
    margin-top: 50rpx;
  }
  .el-button{
    margin-top: 20px;
  }
</style>
