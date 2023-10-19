<template>
  <el-row>默认拓扑导入成功！拓扑参考图:</el-row>
  <div>
        <iframe src="http://localhost:5000/default" id="mobsf" scrolling="no" frameborder="0" style="position:absolute;margin: auto;" ></iframe>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
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
</script>

<style lang="scss" scoped>
.el-main{
  box-sizing: border-box;
  margin: auto auto;
}
</style>
