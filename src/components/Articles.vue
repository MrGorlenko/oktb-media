<template>
<div class='articles'>  
  <h3 class="articles__title">Статьи</h3>
    <ul
    class="articles__items col-lg-4 offset-lg-2 d-lg-flex d-none justify-content-between"
    >
    <li 
    v-for='(theme, index) in themes' 
    :key="index" >
      <p
        v-if='theme.isActive'
        class='articles__item active-button w-100 h-100 '>
        {{theme.theme}}
      </p>
      <p
        v-else
        class='articles__item w-100 h-100 '>
        {{theme.theme}}
      </p>
    </li>
    </ul>
    <!-- <div  class="article__card--wrap">
      <div class="articles__card offset-lg-2 d-flex flex-column mb-1"
        style="top:0px; left:10px">
        <span class="card__subject offset-lg-2">{{articles[0].theme}}</span>
        <span class="card__date offset-lg-2">{{articles[0].date}}</span>
        <p class="card__text offset-lg-2 mb-lg-3">{{articles[0].content}}</p>
      </div>

      <img
        class="articles__img offset-lg-6"
        src="../assets/articles-boy.png"
        alt=""
      />
    </div> -->

</div>
</template>


<script>
import {mapState} from 'vuex'
export default {
name: 'ArticlesComponent',
data(){
  return {
      post:'',
      id:this.$router.currentRoute.params['id']
    }
  },
computed:{
  ...mapState({
        articles: state => state.articlesInfo.Articles,
        themes: state => state.articlesInfo.Themes
    }),
  },
}
</script>

<style lang='scss'>
.articles__items {
  font-size: 16px;
  line-height: 32px;
  letter-spacing: 1px;
}

.active-button{
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
    cursor: pointer;
    color: #fff;
    background-color: rgba(102, 209, 131, 1);
  }
}
</style>