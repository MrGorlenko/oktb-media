import Vue from 'vue'
import Vuex from 'vuex'

import newsInfo from '@/store/newsInfo'
import leadersInfo from '@/store/leadersInfo'
import articlesInfo from '@/store/articlesInfo'
import Videos from '@/store/Videos'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    newsInfo,
    leadersInfo,
    articlesInfo,
    Videos
  }
})