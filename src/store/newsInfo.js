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
