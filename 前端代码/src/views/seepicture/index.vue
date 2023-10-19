<template>
  <div>
      <iframe src="http://localhost:8080" id="mobsf" scrolling="no" frameborder="0" style="position:absolute;margin: auto;" ></iframe>
    </div>
</template>

<script setup>
import axios from 'axios'
// import { seepicture } from '../../api/seepicture'
// import { ElMessage, ElMessageBox } from 'element-plus'
import { ref, onMounted } from 'vue'
const pingall = ref(1)
const changeMobsfIframe = () => {
    const mobsf = document.getElementById('mobsf')
    const deviceWidth = document.body.clientWidth
    const deviceHeight = document.body.clientHeight
    mobsf.style.width = (Number(deviceWidth) - 240) + 'px' // 数字是页面布局宽度差值
    mobsf.style.height = (Number(deviceHeight) - 100) + 'px' // 数字是页面布局高度差
}
onMounted(() => {
  changeMobsfIframe()
  window.onresize = function() {
      changeMobsfIframe()
  }
})
console.log(pingall)
axios({
            method: 'post',
            url: '/seepicture',
            data: { pingall: '1' }
          }).then(res => {
  console.log(pingall.value)
  changeMobsfIframe()
  window.onresize = function() {
      changeMobsfIframe()
  }
})
</script>

<style lang="scss" scoped>
.el-main{
  box-sizing: border-box;
  margin: auto auto;
}
</style>
