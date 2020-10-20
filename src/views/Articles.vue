<template>
  <div>
    <div class="title d-flex align-items-center justify-content-start">
      <div class="green"></div>
        <div class="container">
          <h2>Статьи</h2>
        </div>
      </div>


          <!-- <ul
    class="articles__items switcher col-lg-4 offset-lg-2 d-lg-flex d-none justify-content-between"
    >
    <li 
    v-for='(theme, index) in themes' 
    :key="index" >
      <p
        class='articles__item w-100 h-100 '
        :class="{'active-button': index==0}">
        {{theme.theme}}
      </p>

    </li>
    </ul> -->
    <!-- <div
    v-for='(theme, index) in themes' :key=theme.theme
    class='themes'
    >
      <div v-for='(article) in articles' :key='article.title'
      class=themesTwo
      >
        <div
        v-if='article.theme==theme.theme'
        :class="{'d-none': index != 0}"
        class='art-cat'
        >
          <ArticleCard
          :title = article.title
          :content = article.content
          :date = article.date
          :author = article.author
          :img = article.img
          />
        </div>
      </div>
    </div> -->
<ArticlesComponent/>
  </div>
</template>

<script>
import ArticlesComponent from '@/components/Articles.vue'
export default {
  name: 'Articles',
  components: {
    ArticlesComponent
  }
}
</script>

<style lang="scss" scoped>
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
