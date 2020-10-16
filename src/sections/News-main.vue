<template>
  <div class='News-main '>
    <img class='dots' src="../assets/news-dots.svg" alt="">
    <div class="container-xl news-wrapper">
      <div class="row justify-content-between">
        <div class='col-lg-2 col-12'>
          <h3>Новости</h3>
        </div>
        <div class="col-lg-10 col-12 d-flex justify-content-around flex-wrap">
          <div v-for="item in News" :key="item.date" class='col-lg-5 col-12 news-item'>
            <a class='d-flex flex-column align-items-end w-100 news-link' v-bind:href="item.url">
              <img class='w-98' v-bind:src="item.img" alt="">
              <span class="w-98 date">{{item.date}}</span>
              <p class='w-98'>
                {{item.paragraph}}
              </p>

              <div class='d-block d-lg-none w-98 all-news-link'>
                <a href="#">Все новости 
                  <svg width="44" height="20" viewBox="0 0 44 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M1 10H43M43 10L35.6111 1M43 10L35.6111 19" stroke="#219653" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </a>
              </div>
            </a>
          </div>
          <div class='all-news-link col-5 pl-0'>
          <router-link to="/News" >
            <a href="#">Все новости 
              <svg width="44" height="20" viewBox="0 0 44 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1 10H43M43 10L35.6111 1M43 10L35.6111 19" stroke="#219653" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </a>
          </router-link>
          </div>
          <div class='col-5'></div>
        </div>

        <!-- <div class='col-4'></div> -->
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "News-main",
  data() {
    return {
      News: [
        {
          img: require("../assets/news-item.png"),
          date: '15 фераля 2020',
          paragraph: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Est a auctor ut in maecenas id. Sollicitudin egestas id quis sed viverra ut pellentesque.',
          url: '#'
        },
        {
          img: require("../assets/news-item.png"),
          date: '20 фераля 2020',
          paragraph: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Est a auctor ut in maecenas id. Sollicitudin egestas id quis sed viverra ut pellentesque.',
          url: '#'
        }
      ]
    }
  }

}
</script>

<style lang='scss'>
  
  $animation-duration: .4s ease;

  .News-main{
    padding: 5vh 0;
    background-color:#F2F4F9;
    position: relative;
    .dots{
      position: absolute;
      top: 0;
      right: 0;
    }
    h3{
      font-weight: 600;
      font-size: 40px;
      line-height: 56px;
      color: #000000;
    }
    a:hover{
      text-decoration: none;
    }
  }

  .news-link{
    &:hover{
      p{
        color: #219653;
        transition: color $animation-duration;
      }
    }
  }

  .all-news-link{
    padding-top: 56px;
    a{
      font-style: normal;
      font-weight: bold;
      font-size: 16px;
      line-height: 32px;
      color: #219653;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      transition: color $animation-duration;
      &:hover{
        color: darken($color: #219653, $amount: 10);
        transition: color $animation-duration;
      }
    }
  }

  .news-wrapper{
    height: 95кvh;
  }

  .news-item{
    border-left: 4px solid #66B42F;
    span{
      color: #000000;
      font-size: 16px;
      line-height: 24px;
      margin: 16px 0;
    }
    p{
      font-weight: 600;
      font-size: 32px;
      line-height: 38px;
      letter-spacing: 0.02em;
      color: #000000;
      transition: color $animation-duration;
    }
  }

  @media (max-width: 992px){

    .News-main{
      height: auto;
      h3{
        margin-bottom: 25px;
      }
    }

    .news-wrapper{
      height: auto;
    }

    .all-news-link{
      display: none;
    }

    .news-item{
      p{
        font-weight: 600;
        font-size: 24px;
        line-height: 32px;
      }
    }

    .news-item:nth-child(2){
      display: none;
    }
  }
</style>