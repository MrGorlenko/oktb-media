import Vue from 'vue'
import Vuex from 'vuex'

import newsInfo from '@/store/newsInfo'
import leadersInfo from '@/store/leadersInfo'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    newsInfo,
    leadersInfo
  }
})