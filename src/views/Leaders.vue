<template>
  <div class="leaders_page" id="app">
    <div class="container-fluid p-0">
      <div class="title d-flex align-items-center justify-content-start">
        <div class="green"></div>
        <div class="container">
          <div class="white">
            <h2>Лидеры мнений</h2>
          </div>
        </div>
      </div>
      <div class="container content d-flex flex-lg-row">
        <div class="col-3 pl-0">
          <div class="select">
            <div
              class="w-100"
            >

              <button
                v-for="(category, index) in leadersCategories"
                :key="category.type"
                v-bind:class="{ active: index==0 }"

                class="w-100 mb-3"
              >
                {{ category.label }}
              </button>
            </div>
          </div>
        </div>
        <div class="col-9">
          <div class="row">
            <div
              v-for='leader in leaders' 
              :key='leader.name' 
              class="human">
              <img class='w-100' v-bind:src="leader.img" alt="">
              <div class="green-filter w-100"></div>
              <div class="info d-flex flex-column ">
                <span>{{leader.name}}</span>
                <a v-bind:href="leader.link" > {{leader.link}} </a>
              <div class="audit d-flex align-items-center">
              <img src="../assets/user.svg" alt="">
              <span>{{leader.audience}}</span>
              </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';
import { mapState } from 'vuex';
export default {
  name: 'Leaders',
  data() {
    return {
      activeIndex: -1,
    };
  },
  components: {
    // Header, Footer
    // $
  },
  computed: {
    ...mapState({
      leadersCategories: state => state.leadersInfo.categories,
      leaders: state => state.leadersInfo.leaders
    }),
  },
  methods: {
    onClickBlock(index) {
      if (this.activeIndex == index) {
        this.activeIndex = -1;
      } else {
        this.activeIndex = index;
      }
    },

    ActivateCategory($event, i) {
      this.leadersCategories[i].active = true;
      for (let j = 1; j < 20; j++) {
        this.leadersCategories[i + j].active = false;
      }
      for (let j = 20; j > -1; j--) {
        this.leadersCategories[i - j].active = false;
      }
    },
  },
  mounted() {
    $(".select button").each(function(){
      $(this).click(function(){
        $(this).addClass('active')
        $(this).siblings().removeClass('active')
      })
    })
  }
};
</script>

<style lang="scss" scoped>
@import '../scss/variables';
$distance: 250px;

.green {
  width: $distance;
  height: 8px;
  content: '';
  z-index: 1;
  background-color: $base-green;
}

.white {
  background: #ffffff;
  box-shadow: 20px 24px 32px rgba(108, 137, 164, 0.15);
  width: 733px;
  margin-left: calc(-#{$distance}/ 2);
  padding: 26px 0;
  height: 140px;
  position: relative;
  h2 {
    font-weight: bold;
    font-size: 80px;
    line-height: 88px;
    letter-spacing: 2px;
    color: #1c1642;
    position: absolute;
    right: -145px;
  }
}

.leaders_page {
  background-color: $base-bg-news;
  .content {
    margin-top: 40px;
  }
  .select {
    padding: 16px;
    background-color: #fff;
    border-radius: 8px;
    button {
      padding: 16px 12px;
      background: none;
      color: #1c1642;
      font-size: 20px;
      line-height: 24px;
      font-weight: bold;
    }

    .active {
      background: #2f80ed;
      color: #fff;
      border-radius: 8px;
    }
  }
}
</style>
