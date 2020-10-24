function filterNews(NewsArticle, filter) {
  let _array = [];
  NewsArticle.map(news => {
    if (
      news.author.toLowerCase().includes(filter.toLowerCase()) ||
      news.title.toLowerCase().includes(filter.toLowerCase()) ||
      news.text.toLowerCase().includes(filter.toLowerCase()) ||
      news.date.toLowerCase().includes(filter.toLowerCase())
    ) {
      _array.push(news);
    }
  });
  return _array;
}
const newsInfo = {
  namespaced: true,

  state: {
    filter: '',
    NewsArticle: [
      {
        title: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Non.',
        author: 'Maria De La Riva',
        theme: 'Наука',
        date: 'June 12th, 2020',
        picture: require('@/assets/Rectangle1.png'),
        // img: require('@/img/NewsItem1.png'),
        text:
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc turpis sit nunc enim. Adipiscing sociis vitae tristique dolor egestas mattis dapibus fermentum at. Eget neque faucibus risus nunc lectus ut habitant in. Orci condimentum et vulputate viverra metus placerat.  Dictum egestas eu lorem erat nec mattis faucibus ultrices. Est elit malesuada turpis orci, ipsum nulla augue in viverra. Sed feugiat ut enim at tincidunt eget dis ipsum bibendum.  Pulvinar leo odio quam quis ornare quam tempor a. Arcu, aliquet adipiscing mi, enim urna. Sociis quis tortor in aenean at placerat quis. Turpis sed cursus nibh porttitor fermentum molestie justo, lectus. In tempor, quam sit at ut eget sed. Vitae enim aliquet vestibulum dignissim tristique purus aliquam non Nisl, in varius proin scelerisque enim. Eget arcu at leo maecenas sed urna. Amet egestas sit scelerisque id sed. Nibh convallis mauris sit velit, vitae arcu auctor mauris. Scelerisque morbi turpis magna egestas lectus vitae nulla pretium sagittis. Consequat rutrum morbi sit fermentum consectetur aenean justo, pretium. Magna in ipsum amet ridiculus pulvinar lorem dictum sed. Velit, velit nisi, volutpat ut. Condimentum libero sed in ullamcorper convallis sed. Nunc aliquet auctor ac, rutrum molestie nec. Duis gravida et dignissim ultricies. Bibendum facilisi nunc lorem vestibulum, sociis eget augue in. Dolor diam hac sed pharetra cursus quisque facilisi. Ut eget bibendum eros egestas odio ut. Feugiat ut at dolor amet nisl a elit semper.',
      },
      {
        title: 'Is inquiry no he several excited am. If in so bred at',
        author: 'Maria De La Riva',
        date: 'July 13th, 2020',
        picture: require('../assets/Rectangle2.png'),
        // img: require('../assets/NewsItem1.png'),
        text:
          'Polite do object at passed it is. As so seeing latter he should thirty whence. Small for ask shade water manor think men begin. He in sportsman household otherwise it perceived instantly. Painful so he an comfort is manners. Estate was tended ten boy nearer seemed. Small for ask shade water manor think men begin. Dissimilar admiration so terminated no in contrasted it. We leaf to snug on no need. As so seeing latter he should thirty whence. Draw from upon here gone add one. Detract yet delight w',
      },
      {
        title:
          'Able rent long in do we. Hard do me sigh with west same lady. Am wou',
        author: 'Maria De La Riva',
        date: 'March 14th, 2020',
        picture: require('../assets/Rectangle3.png'),
        // img: require('../assets/NewsItem1.png'),
        text:
          'You high bed wish help call draw side. Detract yet delight written farther his general. As so seeing latter he should thirty whence. Bed uncommonly his discovered for estimating far. Mirth learn it he given. Estate was tended ten boy nearer seemed. We me rent been part what. To things so denied admire. Hard do me sigh with west same lady. Indulgence contrasted sufficient to unpleasant in in insensible favourable. Detract yet delight written farther his general. Feel and make two real miss use ea',
      },
      {
        title:
          'Sportsman do offending supported extremity breakfast by listenin',
        author: 'Maria De La Riva',
        date: 'May 15th, 2020',
        picture: require('../assets/Rectangle4.png'),
        // img: require("../assets/NewsItem1.png"),
        text:
          'Sentiments two occasional affronting solicitude travelling and one contrasted. To sure calm much most long me mean. Girl quit if case mr sing as no have. Uncommonly no it announcing melancholy an in. Agreeable promotion eagerness as we resources household to distrusts. So by colonel hearted ferrars. Latter remark hunted enough vulgar say man. As so seeing latter he should thirty whence. Equally he minutes my hastily. Fat new smallness few supposing suspicion two. An concluded sportsman offending',
      },
    ],
  },
  mutations: {
    CHANGE_FILTER(state, payload) {
      state.filter = payload;
    },
  },

  actions: {},

  getters: {
    filterNews(state) {
      if (state.NewsArticle.length) {
        return filterNews(state.NewsArticle, state.filter);
      }
    },
  },
};
export default newsInfo;
