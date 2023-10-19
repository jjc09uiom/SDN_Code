<template>
  <div>
    <el-upload
      action
      :on-change="updateReason"
      :auto-upload="false"
      accept=".json"
      list-type="multipart/form-data"
    >
      <el-button size="small" type="primary">上传</el-button>
      <div class="el-upload__tip">只能上传JSON文件</div>
    </el-upload>
  </div>
</template>
<script>
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
export default {
  data() {
    return {
      fileList: []
    }
  },
  methods: {
    updateReason(file, fileList) {
      this.fileTransmit(file, fileList)
    },
    fileTransmit(file, fileList, isShow) {
      this.fileList = fileList
      var reader = new FileReader() // 新建一个FileReader
      reader.readAsText(file.raw, 'UTF-8') // 读取文件
      reader.onload = async function(evt) { // 读取文件完毕执行此函数
        const dataJson = evt.target.result
      console.log('submit!')
      ElMessageBox.confirm(
        '确定提交',
        'Warning',
        {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        })
      .then(() => {
        console.log(dataJson)
        axios({
            method: 'post',
            url: '/addflow',
            data: { text: dataJson }
          }).then(res => {
            console.log(1234)
            ElMessage({
              message: '提交成功',
              type: 'success'
            })
          })
          // window.location.reload()
        })
      .catch(() => {
        ElMessage({
            type: 'info',
            message: '取消提交'
          })
          // window.location.reload()
      })
    }
      }
  }
}
</script>
