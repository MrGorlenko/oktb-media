<template>
  <div>
    <div class="title d-flex align-items-center justify-content-start">
      <div class="green"></div>
        <div class="container">
          <h2>Видео</h2>
        </div>
    </div>
    <!-- МЕСТО ДЛЯ ПОИСКА -->
    <div class="container">
      <div class="row">
        <div class="col-6"
        v-for="(video,index) in Videos" :key='index'>
          <VideoItem
          :img=video.picture
          :uploadDate=video.date
          :title=video.Title
          :path='/nVideo/'
          :index=index
          />
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
import VideoItem from '@/components/Video-self'
import {mapState} from 'vuex'
export default {
  name: 'videos',
  components: {
    VideoItem
  },
  computed: {
    ...mapState({
      Videos: state => state.Videos.videos
    })
  }
}
</script>

<style lang='scss' scope>

.title{
  h2 {
    font-weight: bold;
    font-size: 80px;
    line-height: 88px;
    letter-spacing: 2px;
    color: #1c1642;
  }
}

</style>