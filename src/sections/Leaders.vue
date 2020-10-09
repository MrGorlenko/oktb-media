<template>
  <div class="leaders">
    <img class='ellipse' src="../assets/Ellipse.svg" alt="">
    <img class='dots' src="../assets/dots-bg-1.svg" alt="">
    <div class="container-lg d-flex justify-content-center flex-column">
      <div class="w-100 title d-flex align-items-center">
        <h3 class='col-6'>Лидеры мнений</h3>
        <div class="col-6 green"></div>
      </div>
      <div class="w-100 people d-flex">
        <div 
        v-for='leader in leaders' 
        :key='leader.name' 
        class="human col-3"
        >
          <img class='w-100' v-bind:src="leader.img" alt="">
          <div class="info d-flex flex-column ">
            <span>{{leader.name}}</span>
            <a v-bind:href="leader.link" > {{leader.link}} </a>
            <div class="audit d-flex align-items-center">
              <img src="../assets/user.svg" alt="">
              <span>{{leader.audience}}</span>
            </div>
          </div>
        </div>
      </div>
      <a class='d-flex' href="#">
        <button>Все Лидеры <img src="../assets/button-arrow.svg" alt=""></button>
      </a>
    </div>

  </div>
</template>

<script>

export default {
  name: 'leaders',
  data() {
    return {
      leaders: [
        {
          name: 'Nickname1',
          link: 'url-link-to-her-page',
          img: require('../assets/leader-1.png'),
          audience: 1000
        },
        {
          name: 'Nickname2',
          link: 'url-link-to-his-page',
          img: require('../assets/leader-2.png'),
          audience: 1000
        },
        {
          name: 'Nickname3',
          link: 'url-link-to-her-page',
          img: require('../assets/leader-3.png'),
          audience: 1000
        },
        {
          name: 'Nickname4',
          link: 'url-link-to-his-page',
          img: require('../assets/leader-4.png'),
          audience: 1000
        }

      ]
    }
  },
  methods: {
    mouseOver: function() {
      
    }
  }
}
</script>

<style lang="scss" scope>

@import '../scss/variables';

  .leaders{
    background-color: #f2f4f9;
    padding-bottom: 80px;
      position: relative;
      .ellipse{
        position: absolute;
        top: -30%;
        left: 0%;
      }
      .dots{
        position: absolute;
        left: 0;
        top: -10%;  
      }
    .title{
      h3{
          font-weight: bold;
          font-size: 65px;
      }
      .green{
        height: 8px;
        background-color: $base-green;
      }
    }

    .human{
      position: relative;
      cursor: pointer;
      margin-top: 60px;
      .info{
        position: absolute;
        bottom: 10px;
        left: 30px;
        opacity: 0;
        transition: opacity .3s ease;
        span{
        font-weight: bold;
        font-size: 24px;
        color: #fff;
        }
        a{
          display: block;
          background: #fff;
          color: #2F80ED;
          font-weight: 500;
          font-size: 16px;
          padding: 4px 8px;
        }
        .audit{
          margin-top: 8px;
          span{
            font-style: normal;
            font-weight: bold;
            font-size: 16px;
            color: #fff;
            margin-left: 12px;
          }
        }
      }
      &:hover{
        .info{
          opacity: 1;
          transition: opacity .3s ease;
        }
      }
    }

    a{
      &:hover{
        text-decoration: none;
      }
    }

    button{
      width: 234px;
      height: 64px;
      background-color: $base-green;
      color: #fff;
      border-radius: 10px;
      margin: auto;
      margin-top: 48px;
      transition: color .3s ease;
      cursor: pointer;
      z-index: 3;
      &:hover{
        background-color: darken($color: $base-green, $amount: 10);
        transition: color .3s ease;
      }
    }
  }
</style>