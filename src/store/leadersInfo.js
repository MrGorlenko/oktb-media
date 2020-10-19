const leadersInfo = {
  namespaced: true,

  state: {
     leaders: [
     {
        name: 'Nickname1',
        link: 'url-link-to-her-page',
        img: require('../assets/leader-1.png'),
        audience: 1000,
        category: 'leader'
      },
       {
        name: 'Nickname2',
        link: 'url-link-to-his-page',
        img: require('../assets/leader-2.png'),
        audience: 1000,
        category: 'blogger'
      },
      {
        name: 'Nickname3',
        link: 'url-link-to-her-page',
        img: require('../assets/leader-3.png'),
        audience: 1000,
        category: 'leader'
      }, 
      {
        name: 'Nickname4',
        link: 'url-link-to-his-page',
        img: require('../assets/leader-4.png'),
        audience: 1000,
        category: 'leader'
      }
    ],
    categories: [
      {
        type: 'leader',
        label: 'Лидеры мнений',
        active: true
      },
      {
        type: 'blogger',
        label: 'Блоггеры',
        active: false
      }
    ] 
  },
  mutations: {
    
  },

  actions: {
    
  },

  getters: {
    
  },
};
export default leadersInfo;
