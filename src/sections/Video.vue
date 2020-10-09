<template>
  <div class="video">
    <div class="container-lg">
      <div class="row justify-content-between">
        <videoItem/>
        <videoItem/>
        <videoItem/>
        <videoItem/>
      </div>
    </div>
  </div>
</template>

<script>

import videoItem from '@/components/Video-self'

export default {
  name: 'Video',
  components: {
    videoItem
  },
}
</script>

<style lang="scss" scope>
.video{
  background-color: #f2f4f9;
  padding-bottom: 160px;
}
</style>
