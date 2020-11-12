<template>
  <div class="articles">
    <img class="ellipse" src="../assets/Ellipse.svg" alt="" />

    <div class="row justify-content-between container-xl m-auto">
      <div class="col-lg-2 col-sm-12">
        <h3 class="articles__title">Статьи</h3>
      </div>
    </div>
    <div class="articles__wrapp  ">
      <swiper
          class="switcher articles__items slider d-lg-block d-block"
          ref="mySwiper"
          :options="swiperOptions" >
        <ul
          class="articles__items switcher col-lg-4 offset-lg-2 d-lg-flex justify-content-between"
        >
          <swiper-slide style="justify-content: space-between; display: flex;">
          <li v-for="(theme, index) in themes" :key="index">
            <p class="articles__item item w-100 h-100"
               :class="{ 'activeButton': index == 0 }">
              {{ theme.theme }}
            </p>
          </li>
          </swiper-slide>
        </ul>
      </swiper>

      <div v-for="(theme, jindex) in themes" :key="theme.theme" class="themes">
        <div
          v-for="(article, index) in articles"
          :key="article.title"
          class="themesTwo"
        >
          <div
            v-if="article.theme === theme.theme && article.hot === true"
            :class="{ 'd-none': jindex != 0 }"
            class="art-cat"
          >
            <ArticleCard
              :title="article.title"
              :content="article.content"
              :date="article.date"
              :author="article.author"
              :img="article.img"
              :path="/nArticle/"
              :index="index"
            />
          </div>
        </div>
      </div>
      <div
        class="container-lg d-flex justify-content-lg-end justify-content-center"
      >
        <router-link
          to="/Articles"
          class=" d-flex align-items-center justify-content-between"
        >
          <div class="link-to-all">
            Все статьи
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
//import Articles from '@/components/Articles'
import ArticleCard from '@/components/subcomponents/Article-Card';
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper';
import 'swiper/swiper-bundle.css';
import { mapState } from 'vuex';
//import $ from 'jquery';

export default {
  name: 'Articles1',
  components: {
    // Articles
    ArticleCard,
    Swiper,
    SwiperSlide,
  },
  computed: {
    ...mapState({
      articles: state => state.articlesInfo.Articles,
      themes: state => state.articlesInfo.Themes,
    }),
    swiper() {
      return this.$refs.mySwiper.$swiper;
    },
  },
  directives: {
    swiper: directive,
  },
  data: function () {
    return {
      swiperOptions: {
        slidesPerView: 4,
        spaceBetween: 15,
      }
    }
  },
  mounted() {
    const tabs = document.querySelectorAll('ul li .item');
    const contents = document.querySelectorAll('.art-cat');
    let len = this.articles.length;
    tabs.forEach((tab, value) => {
      tab.addEventListener('click', () => {
        tabs.forEach(el => {
          el.classList.remove('activeButton');
        })
        tab.classList.add('activeButton')
        contents[value].classList.remove('d-none')
        for (let j = 1; j < len; j++) {
          if(contents[value + j]) {
            contents[value + j].classList.add('d-none')
          }
          if (contents[value - j]) {
            contents[value - j].classList.add('d-none')
          }
        }
      })
    })

    }
  }
</script>

<style lang="scss" scope>
@import '../scss/variables';

.articles {
  position: relative;
  background-image: url('~@/assets/dots-articles.svg');
  background-repeat: no-repeat;
  background-color: #f2f4f9;
  padding-bottom: 100px;
  //overflow: hidden;
  ul {
    li {
      list-style-type: none;
      cursor: pointer;
      p {
        margin-bottom: 0;
      }
    }
  }
}
.ellipse {
  position: absolute;
  top: -15%;
  left: -5%;
}
.articles__title {
  font-family: 'San Francisco', sans-serif;
  font-size: 80px;
  font-style: normal;
  font-weight: 700;
  line-height: 88px;
  letter-spacing: 2px;
  text-align: left;
}
.articles__items {
  font-size: 16px;
  line-height: 32px;
  letter-spacing: 1px;
}

.active-button {
  color: #fff;
  background-color: rgba(102, 209, 131, 1);
}

.articles__item {
  text-transform: uppercase;
  text-align: center;
  list-style: none;
  box-sizing: border-box;
  padding: 6px 4px;
  height: 48px;
  width: 112px;

  &:hover {
    @media screen and (min-width: 576px) {
      cursor: pointer;
      color: #fff;
      background-color: rgba(102, 209, 131, 1);
    }
  }
}
.article__card--wrap {
  position: relative;
  height: 420px;
}

.articles__card {
  position: relative;
  top: 0px;
  left: 10px;
  z-index: 5;
  height: auto;
  width: 642px;
  left: 325px;
  top: 3088px;
  border-radius: 15px;
  background-color: #fff;
  box-shadow: 20px 24px 32px 0px rgba(108, 137, 164, 0.15);
  &::before {
    content: '';
    position: relative;
    top: 70px;
    right: 220px;
    height: 8px;
    background-image: url('~@/assets/line.svg');
    background-repeat: no-repeat;
  }
}
.card__subject {
  height: 28px;
  width: fit-content;
  padding-left: 5px;
  padding-right: 5px;
  margin-top: 32px;
  padding-top: 3px;
  text-align: center;
  box-sizing: border-box;
  border-radius: 10px;
  color: #fff;
  background: black;
}

.card__date {
  margin-top: 10px;
  margin-bottom: 10px;
  color: #828282;
}
.card__text {
  width: 480px;
  font-style: normal;
  font-weight: 600;
  font-size: 32px;
  line-height: 38px;
  letter-spacing: 0.02em;

  color: #000000;
}
.articles__img {
  position: relative;
  top: -200px;
  left: -16px;
  z-index: 3;
  height: 271px;
  width: 584px;
  border-radius: 15px;
}

.swiper {
  .swiper-pagination-bullet-custom {
    opacity: 0.7;
    &:hover {
      opacity: 1;
    }
    &.swiper-pagination-bullet-active {
      opacity: 1;
      color: #fff;
      background: #007aff;
    }
  }
}

@media (max-width: 576px) {
  .articles {
    padding-bottom: 70px;
  }
  .ellipse {
    //position: absolute;
    top: -3%;
    left: -9%;
  }
  .articles__title {
    font-size: 32px;
    line-height: 120%;
  }

  .active-button {
    padding: 24px 8px;
  }

  .articles__items {
    margin-top: 40px;
    margin-bottom: 60px;
  }
  .article__card--wrap {
    display: none;
  }
  .card__wrapp {
    background-color: transparent;
    box-shadow: none;
  }

  .articles__wrapp {
    ul {
      display: flex;
      li {
        width: 25%;
      }
    }
  }
}
</style>
