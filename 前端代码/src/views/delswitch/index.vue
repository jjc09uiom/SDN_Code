<!-- 删除交换机 -->
<template>
  <el-form :model="form" label-width="290px" ref="formRef" :rules="rules">
    <el-form-item label="请输入要删除的交换机名：" prop="switch">
          <el-input v-model="form.switch" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit(form)">提交</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'
// import axios from 'axios'
const formRef = ref(null)
const form = ref({
  switch: ''
})
const onSubmit = () => {
  formRef.value.validate((valid) => {
  if (valid) {
    ElMessageBox.confirm('确定删除', 'Warning', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
    .then(() => {
      axios({
            method: 'post',
            url: '/delswitch',
            data: { switch: form.value.switch }
          }).then(res => {
        ElMessage({
          type: 'success',
          message: '删除成功'
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
