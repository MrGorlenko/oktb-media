<template>
  <div class="video">
    <div class="container-lg">
<!--       <div class="row justify-content-between">
 -->        
 <div class="d-flex flex-column flex-sm-row justify-content-between">
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

@media (max-width: 375px) {
.bord{
  padding-left: 15px;
  padding-right: 15px;
  border-radius: 0;
  border-left: 4px solid $base-green;
    }
}
</style>
