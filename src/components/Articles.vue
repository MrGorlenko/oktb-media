<template>
  <div class="articles ">
    <div class="articles__wrapp container-xl ">
      <div class="row justify-content-between">
        <div class="col-lg-2 col-sm-12">
          <h3 class="articles__title">Статьи</h3>
        </div>
      </div>
      <div class="row justify-content-between">
        <ul
          class="articles__items col-lg-4 offset-lg-2 d-flex justify-content-between"
        >
          <li class="articles__item ">Статьи</li>
          <li class="articles__item ">Статьи</li>
          <li class="articles__item ">Статьи</li>
          <li class="articles__item ">Статьи</li>
        </ul>
      </div>
      <div class="article__card--wrap">
        <div
          class="articles__card offset-lg-2 d-flex flex-column mb-1"
          style="top:0px; left:10px"
          v-for="(article, index) in articles.slice(1)"
          :key="index"
        >
          <span class="card__subject offset-lg-2">{{ article.subject }}</span>
          <span class="card__date offset-lg-2">{{ article.date }}</span>
          <p class="card__text offset-lg-2 mb-lg-3">{{ article.title }}</p>
        </div>

        <img
          class="articles__img offset-lg-6"
          src="../assets/articles-boy.png"
          alt=""
        />
      </div>
    </div>
    <ArticlesCard />
  </div>
</template>

<script>
import ArticlesCard from '@/components/Articles-Card';

export default {
  name: 'Articles',
  components: {
    ArticlesCard,
  },
  data() {
    return {
      articles: [
        {
          subject: 'Наука',
          title:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          img: require('../assets/articles1.png'),
          date: '15 фераля 2020',
          content:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Est a auctor ut in maecenas id. Sollicitudin egestas id quis sed viverra ut pellentesque.',
          url: '#',
        },

        {
          subject: 'Наука',
          title:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet, varius leo eu, sagittis, dictumst ',
          img: require('../assets/articles2.png'),
          date: '15 фераля 2020',
          content:
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Est a auctor ut in maecenas id. Sollicitudin egestas id quis sed viverra ut pellentesque.',
          url: '#',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scope>
.articles {
  background-image: url('~@/assets/dots-articles.svg');
  background-repeat: no-repeat;
  background-color: #f2f4f9;
  padding-bottom: 30px;
}

.articles__title {
  font-family: 'San Francisco' sans-serif;
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

.articles__item {
  text-transform: uppercase;
  text-align: center;
  list-style: none;
  box-sizing: border-box;
  padding-top: 8px;
  // background-color: #fff;
  height: 48px;
  width: 112px;

  &:hover {
    cursor: pointer;
    color: #fff;
    background-color: rgba(102, 209, 131, 1);
  }
}
.article__card--wrap {
  position: relative;
}

.articles__card {
  position: relative;
  top: 0px;
  left: 10px;
  z-index: 5;
  height: 284px;
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
  width: 52px;
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
</style>
