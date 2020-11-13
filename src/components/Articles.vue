<template>
  <div class="articles">
    <swiper
      class="switcher articles__items slider d-lg-block
       d-block"
      ref="mySwiper"
      :options="swiperOptions"
    >
      <ul
          class="articles__items switcher col-lg-4 offset-lg-2 d-lg-flex justify-content-between"
      >
        <swiper-slide style="justify-content: space-between; display: flex;">
          <li v-for="(theme, index) in tThemes" :key="index"
              >
            <p class="articles__item item w-100 h-100"
               :class="{ 'activeButton': index == 0 }">
              {{ theme.theme }}
            </p>
          </li>
        </swiper-slide>
      </ul>
    </swiper>
    <div v-for="(theme, jindex) in tThemes" :key="theme.theme" class="themes">
      <div
          v-for="(article, index) in tArticles"
          :key="article.index"
          class="themesTwo">
        <div  v-if="article.theme === theme.theme && article.hot === true"
              :class="{ 'd-none': jindex != 0 }"
              class="art-cat">
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
  </div>
</template>

<script>
import ArticleCard from '@/components/subcomponents/Article-Card';
//import Paginate from 'vuejs-paginate';
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper';
import 'swiper/swiper-bundle.css';
import { mapState } from 'vuex';

export default {
  name: 'ArticlesComponent',

  directives: {
    swiper: directive,
  },
  components: {
    ArticleCard,
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      swiperOptions: {}
    }
  },
  computed: {
    ...mapState({
      articles: state => state.articlesInfo.Articles,
      themes: state => state.articlesInfo.Themes,
      tArticles: state => state.articlesInfo.tArticles,
      tThemes: state => state.articlesInfo.tThemes,
    }),
    swiper() {
      return this.$refs.mySwiper.$swiper;
    }
  },
  methods: {  },
  mounted() {
    const tabs = document.querySelectorAll('ul li .item');
    const contents = document.querySelectorAll('.art-cat');
    let len = this.themes.length;
    tabs.forEach((tab, value) => {
      tab.addEventListener('click', () => {
        tabs.forEach(el => {
          el.classList.remove('activeButton');
        })
        tab.classList.add('activeButton')
        contents[value].classList.remove('d-none')
        for (let j = value + 1; j < len; j++) {
          if(contents[value + j]) {
            contents[value + j].classList.add('d-none')
          }
          if (contents[value - j]) {
            contents[value - j].classList.add('d-none')
          }
        }

        console.log(value)
      })
    })
  }
}
</script>

<style lang="scss">
@import '../scss/variables';
$distance: 250px;


.articles__items {
  font-size: 16px;
  line-height: 32px;
  letter-spacing: 1px;
}
.activeButton {
  display: block;
}
.green {
  width: $distance;
  height: 8px;
  content: '';
  z-index: 1;
  background-color: $base-green;
}

.activeButton {
  color: #fff;
  background-color: rgba(102, 209, 131, 1);
}

.pagination {
  padding: 6px 4px;
}
.articles__item {
  text-transform: uppercase;
  text-align: center;
  list-style: none;
  box-sizing: border-box;
  height: 48px;
  width: 112px;

  &:hover {
    cursor: pointer;
    color: #fff;
    background-color: rgba(102, 209, 131, 1);
  }
}
</style>
