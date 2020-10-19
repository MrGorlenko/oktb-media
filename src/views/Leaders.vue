<template>
  <div class="leaders_page" id="app">
    <div class="container-fluid p-0">
      <div class="title d-flex align-items-center justify-content-start">
        <div class="green"></div>
        <div class="white">
          <h2>Лидеры мнений</h2>
        </div>
      </div>
      <div class="container content">
        <div class="col-3">
          <div class="select">
            <div
              v-for="(category, index) in leadersCategories"
              :key="category.type"
              class="w-100"
            >
              <button
                v-bind:class="{ active: activeIndex === index }"
                @click="onClickBlock(index)"
                class="w-100 mb-3"
              >
                {{ category.label }}
              </button>

              <!--  <button v-if="category.active == true" class="active w-100">
                {{ category.label }}
              </button> 
              <button
                v-on:click="ActivateCategory($event, i)"
                v-else
                class="w-100"
              >
                {{ category.label }}
              </button> -->
            </div>
          </div>
        </div>
        <div class="col-9"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
// import Header from '../components/Header';
// import Footer from '../components/Footer';
export default {
  name: 'Leaders',
  data() {
    return {
      activeIndex: -1,
    };
  },
  components: {
    // Header, Footer
  },
  computed: {
    ...mapState({
      leadersCategories: state => state.leadersInfo.categories,
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
