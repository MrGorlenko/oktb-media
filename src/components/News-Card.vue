<template>
  <div class="search container-xl align-items-center">  
    <div class="container-lg d-flex flex-column align-items-end">
      <div class="w-100 card__wrapp d-flex flex-column-reverse flex-sm-row justify-content-around align-items-center mb-3"
        v-for="(article, index) in themeArticles" :key="index">
          <div class="article__item d-flex justify-content-between flex-column col-xl-7" >
              <p class="w-100 art__card mb-1">{{article.text}}</p>
              <div class="wrap mb-3">
              <span><img v-bind:src="article.contImg"></span>
              <span class="w-100 art__content">{{article.content}}</span>
              </div>
            <div class="w-100 art__item--link col-lg-6 pl-0 mt-sm-5 mt-md-1">
          <a href="#">Узнать больше
              <svg width="44" height="20" viewBox="0 0 44 20" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M1 10H43M43 10L35.6111 1M43 10L35.6111 19" stroke="#219653" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
          </a>
        </div>
      </div>

      <div class="art__img--news col-lx-6" >
        <img v-bind:src="article.img" alt="">
      </div>
    </div>
  </div>
      </div> 
</template>

<script>

export default {
    name:"News_Card",
    data() {
      return {
        themeArticles: [
        {
          title: 'Наука',
          img: require('../assets/Rectangle1.png'),
          text:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          contImg:require('../assets/photo-min.png'),
          content:'By Maria De La Riva, Updated in June 13th, 2020',
          isActive: true

        },
        {
          title: 'Техника',
          text:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          img: require('../assets/Rectangle2.png'),
          content:'By Maria De La Riva, Updated in June 13th, 2020',
          contImg:require('../assets/photo-min.png'),
          isActive: false
        },
        {
          title: 'Медиа',
          text:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          img: require('../assets/Rectangle3.png'),
          content:'By Maria De La Riva, Updated in June 13th, 2020',
          contImg:require('../assets/photo-min.png'),
          isActive: false
        },
        {
          title: 'Досуг',
          text:'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          img: require('../assets/Rectangle4.png'),
          content:'By Maria De La Riva, Updated in June 13th, 2020',
          contImg:require('../assets/photo-min.png'),
          isActive: false
        }
      ],
      }
    },
}
</script>

<style lang="scss">
@import '../scss/variables';
@media (max-width:576px) {
  .art__img--news>img{
  width:280px;
}
 .card__wrapp{
  padding: 0;
  border-radius: 0;
  border-left: 4px solid $base-green;

  }
}


</style>