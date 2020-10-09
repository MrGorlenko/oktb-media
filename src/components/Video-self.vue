<template>
  <div class="video-item w-48">
    <div class='content h-100'>
      <div class="picture-wrapper d-flex justify-content-center align-items-center flex-column">
        <img class='run' src="../assets/start-video.svg" alt="">
        <img class='w-100 main-pic h-100' src="../assets/video-1.png" alt="">
        <div class="darken w-100 h-100"></div>
      </div>
      <span>15.03.2020</span>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'videoItem'
}
</script>

<style lang='scss' scoped>

  @import '../scss/variables';

  .video-item{
    background: #FFFFFF;
    box-shadow: 20px 24px 32px rgba(108, 137, 164, 0.15);
    border-radius: 15px;
    cursor: pointer;
    height: 582px;
    padding: 40px;
    margin-bottom: 44px;

    &:hover{
      .content .picture-wrapper{
        .darken, .run{
          opacity: 1;
          transition: opacity .4s ease;
        }
      }
    }

    .content{
      padding-left: 28px;
      border-left: 4px solid $base-green;
      span{
        color: #828282;
        font-size: 14px;
        line-height: 20px;
        margin-top: 28px;
        display: block;
      } 
      p{
        font-weight: 600;
        font-size: 28px;
        line-height: 36px;
        letter-spacing: 0.02em;
        color: #000000;
        margin-top: 24px;
      }
    }

    .picture-wrapper{
      position: relative;
      height: 275px;
      .run{
        z-index: 2;
        opacity: 0;
        transition: opacity .4s ease;
      }
      .darken{
        position: absolute;
        top: 0;
        left: 0;
        background-color: rgba($color: #000000, $alpha: .2);
        content: '';
        border-radius: 15px;
        opacity: 0;
        transition: opacity .4s ease
      }
      .main-pic{
        position: absolute;
        top: 0;
        left: 0;
        border-radius: 15px;
      }
    }


  }
</style>