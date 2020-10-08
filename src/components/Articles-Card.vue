<template>
  <div class="article__card ">
    <div class="card__wrap container-xl">
      <div class="row">
        <div class="col-lg-6 alert-dark">
          <span>{{ item.date }}</span>
        </div>
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
.article__card {
  background-color: #f2f4f9;
}

.article__card {
  height: 518px;
  width: 1060px;
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
