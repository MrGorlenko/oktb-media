<template>
  <div class="video">
    <div class="container-lg pl-lg-1 pr-lg-1 pl-0 pr-0">
       
      <div class="d-flex flex-column flex-lg-row flex-wrap justify-content-between">
        <div
        v-for='(video, index) in videos' :key=index
        class='col-lg-5-8 h-auto col-12 video-wrapper'>
        <videoItem
        :img=video.picture
        :uploadDate=video.date
        :title=video.title
        :path='/nVideo/'
        :index=index
        v-if="index<=4"
        />
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import videoItem from '@/components/Video-self'
import {mapState} from 'vuex'
export default {
  name: 'Video',
  components: {
    videoItem
  },
  computed: {
    ...mapState({
        videos: state => state.Videos.videos,
    }),
  }
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
.video-wrapper{
    &:nth-child(3), &:nth-child(4){
    display: none;
  }
}

}
</style>
