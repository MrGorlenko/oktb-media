<template>
  <div class="article__card mt-10">
  <div class="container-lg d-flex flex-column align-items-end">
    <div class="w-100 card__wrapp d-flex flex-column-reverse flex-sm-row justify-content-around align-items-center"
         v-for="(article, index) in articles" :key="index">

      <div class="article__item d-flex justify-content-between flex-column col-xl-6" >
        <span class="w-100 art__date pt-5 pt-sm-0"> {{article.date}}</span>
        <p class="w-100 art__card">{{article.title}}</p>
        <p class="w-100 art__content">{{article.content}}</p>
        <div class="w-100 art__item--link col-lg-6 pl-0 mt-sm-5 mt-md-1">
          <a href="#">Узнать больше
              <svg width="44" height="20" viewBox="0 0 44 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1 10H43M43 10L35.6111 1M43 10L35.6111 19" stroke="#219653" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
          </a>
        </div>
      </div>

      <div class="art__img col-lx-6 alert-dark" >
        <img v-bind:src="article.img" alt="">
      </div>
    </div>
    <a class='articles-all' href="#">
      <button class=" btn-lg">Все статьи <img src="../assets/button-arrow.svg" alt=""> </button>
    </a>
  </div>
  </div>
</template>

<script>
export default {
  name: 'ArticlesCard',
  data() {
    return {
      articles: [
        {
          subject: 'Наука',
          title:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          img: require('../assets/articles1.png'),
          date: '15 фераля 2020',
          content:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mi eros venenatis fames sit. Facilisis nunc fringilla aliquam lectus proin elit aliquam. Nulla nunc sit arcu duis porta porttitor non fermentum, quisque.' ,
          url: '#',
          
        },

        {
          subject: 'Наука',
          title:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          img: require('../assets/articles2.png'),
          date: '15 фераля 2020',
          content:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mi eros venenatis fames sit. Facilisis nunc fringilla aliquam lectus proin elit aliquam. Nulla nunc sit arcu duis porta porttitor non fermentum, quisque.' ,
          url: '#',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scope>

@import '../scss/variables';

.article__card{
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
      cursor: pointer;
      z-index: 300;
      &:hover{
        background-color: darken($color: $base-green, $amount: 10);
        transition: color .3s ease;
      }
    }
}

.card__wrapp{
  padding: 40px;
  width: 1060px;
  margin: 0 auto;
  border-radius: 15px;
  background-color: #fff;
  box-shadow: 20px 24px 32px 0px rgba(108, 137, 164, 0.15);
  &:first-child{
    margin-bottom: 32px;
  }
}

.card__subject {
  height: 28px;
  width: 52px;
  margin-top: 32px;
  padding-top: 3px;
  text-align: center;
  box-sizing: border-box;
  border-radius: 10px;
  color: #fff;
  background: black;
}

.art__date {
  margin-bottom: 26px;
  color: #828282;
}
.art__card {
  position: relative;
width: 572px;
margin-bottom: 40px;
  font-style: normal;
  font-weight: 600;
  font-size: 32px;
  line-height: 38px;
  letter-spacing: 0.02em;
  color: #000000;
 
}
.art__content{
  height: 120px;
//width: 572px;
font-size: 16px;
font-style: normal;
font-weight: 400;
line-height: 24px;
letter-spacing: 0,03em;
text-align: left;
color: rgba(79, 79, 79, 1);
}
.article__item{
  position: relative;
  border-left: 4px solid $base-green;
  padding-left: 24px;
}
.art__item--link{
    a{
     
      font-style: normal;
      font-weight: bold;
      font-size: 16px;
      line-height: 32px;
      color: #219653;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      &:hover{ 
        text-decoration: none;
        color: darken($color: #219653, $amount: 10);

      }
    }
}
.art__img {
  height: 438px;
  width: 356px;
  border-radius: 15px;
}

@media (max-width:375px) {
  .card__wrapp{
  padding: 0;
  border-radius: 0;
  border-left: 4px solid $base-green;

  }
  .article__item{
    //width: 324px;
    border: none;
  }
.art__img{
  width: 324px;
  height: 322px;
}
.art__img>img{
  width: 324px;
  height: 322px;
  }
.art__date{
  font-size: 16px;
  line-height: 24px;
  color:  rgba(0, 0, 0, 1);
} 
.art__card{
  font-size: 24px;
line-height: 32px;
} 
}
</style>
