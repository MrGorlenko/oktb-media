<template>
  <div class="article__card mt-10">
  <div class="container-xl">
    <div class="card__wrapp d-flex justify-content-around mb-3"
         v-for="(article, index) in articles" :key="index">

      <div class="article__item d-flex justify-content-between flex-column col-xl-6" >
        <span class="art__date offset-1"> {{article.date}}</span>
        <p class="art__card offset-1">{{article.title}}</p>
        <p class="art__content offset-1">{{article.content}}</p>
        <div class="art__item--link offset-1 col-lg-6 pl-0">
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
    <div class="offset-9 mt-3">
              <button class="btn btn-success btn-lg">Все статьи</button>
</div>
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
.card__wrapp{
  height: 518px;
  width: 1060px;
  margin: 0 auto;
  border-radius: 15px;
  background-color: #fff;
  box-shadow: 20px 24px 32px 0px rgba(108, 137, 164, 0.15);
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
  margin-top: 40px;
  margin-bottom: 26px;
  color: #828282;
}
.art__card {
  position: relative;
 height: 108px;
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
  &::before{
      content: " ";
    width: 438px;
    position: relative;
    top: 264px;
    left: -212px;
    transform: rotate(90deg);
    border: 1px solid #66B42F;
  //background-image: url('~@/assets/line-art.svg');
  
  }
}
.art__item--link{
    padding-top: 56px;
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
  margin-top: 40px;
 height: 438px;
width: 356px;
border-radius: 15px;

}
</style>
