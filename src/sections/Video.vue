<template>
  <div class="video">
    <div class="container-lg pl-lg-1 pr-lg-1 pl-0 pr-0">
       
      <div class="d-flex flex-column flex-lg-row flex-wrap justify-content-between">
        <div
        v-for='(video, index) in videos' :key=index
        class='col-lg-5-8 h-auto col-12 video-wrapper'>
        <VideoItem
        :img=video.picture
        :uploadDate=video.date
        :title=video.Title
        :path='/nVideo/'
        :index=index
        v-if="index<=4"
        />
        </div>
      </div>
      <div class="container-lg d-flex justify-content-lg-end justify-content-center">
          <router-link
            to="/Videos"
            class=" d-flex align-items-center justify-content-between"
          >
          <div class="link-to-all">
            Все видео
            <svg
              width="44"
              height="20"
              viewBox="0 0 44 20"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M1 10H43M43 10L35.6111 1M43 10L35.6111 19"
                stroke="white"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              />
            </svg>
          </div>
          </router-link>
      </div>
    </div>
  </div>
</template>

<script>

import VideoItem from '@/components/Video-self'
import {mapState} from 'vuex'
export default {
  name: 'Video',
  components: {
    VideoItem
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

  .link-to-all{
    display: block;
    margin: auto;
    margin-top: 50px;
  }
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
