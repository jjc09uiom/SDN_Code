<template>
  <div class="navbar">
    <Breadcrumb />
  </div>
</template>

<script setup>
import Breadcrumb from './components/breadcrumb.vue'
</script>

<style lang="scss" scoped>
.navbar {
  width: 100%;
  height: 60px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  padding: 0 16px;
  display: flex;
  align-items: center;
  box-sizing: border-box;
  position: relative;
}
</style>
