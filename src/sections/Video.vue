<template>
  <div class="video">
    <div class="container-lg pl-lg-1 pr-lg-1 pl-0 pr-0">
<!--       <div class="row justify-content-between">
 -->        
 <div class="d-flex flex-column flex-lg-row flex-wrap justify-content-between">
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

<style lang="scss" >

@import '../scss/variables';

.video{
  background-color: #f2f4f9;
  padding-bottom: 160px;
}

@media (max-width: 576px) {

.video{
  overflow: hidden;
}
.bord{
  padding-left: 15px;
  padding-right: 15px;
  border-radius: 0;
  border-left: 4px solid $base-green;
    }
}
</style>
