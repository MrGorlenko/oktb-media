<template>
  <div class="leaders" v-if="leaders.length > 0">
    <img class="ellipse" src="../assets/Ellipse.svg" alt="" />
    <img class=" dots" src="../assets/dots-bg-1.svg" alt="" />
    <div class="container-lg d-flex justify-content-center flex-column">
      <div
        class="w-100 title d-flex align-items-center flex-wrap justify-content-end"
      >
        <h3 class="col-lg-6 col-12 p-0">Лидеры Мнений</h3>

        <div class="col-lg-6 col-6 green"></div>
      </div>
      <div class="w-100 people d-lg-flex d-none flex-wrap">
        <div
          v-for="leader in leaders"
          :key="leader.name"
          class="human col-3"
          :class="{ 'd-none': !leader.top }"
        >
          <img class="w-100" v-bind:src="leader.img" alt="" />
          <div class="green-filter"></div>
          <div class="info d-flex flex-column ">
            <span>{{ leader.name }}</span>
            <a v-bind:href="leader.link"> {{ leader.link }} </a>
            <div class="audit d-flex align-items-center">
              <img src="../assets/user.svg" alt="" />
              <span>{{ leader.audience }}</span>
            </div>
          </div>
        </div>
      </div>

      <swiper class="d-lg-none d-block" ref="mySwiper" :options="swiperOptions">
        <swiper-slide

          v-for="leader in leaders"
          :key="leader.name"
          class="human"
        >
          <img
            class="w-100"
            :class="{ 'd-none': !leader.top }"
            v-bind:src="leader.img"
            alt=""
          />
          <div class="green-filter w-100"></div>
          <div class="info d-flex flex-column ">
            <span>{{ leader.name }}</span>
            <a v-bind:href="leader.link"> {{ leader.link }} </a>
            <div class="audit d-flex align-items-center">
              <img src="../assets/user.svg" alt="" />
              <span>{{ leader.audience }}</span>
            </div>

          </div>
        </swiper-slide>
      </swiper>

      <div class="link-to-all">
        <router-link class='w-100 d-flex align-items-center justify-content-between' to="/Leaders">
        Все Лидеры <img src="../assets/button-arrow.svg" alt="">
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper';
import { mapState } from 'vuex';
import 'swiper/swiper-bundle.css';
export default {
  name: 'leaders',
  data() {
    return {
      swiperOptions: {
        pagination: {
          el: '.swiper-pagination',
        },
        slidesPerView: 1.5,
        spaceBetween: 20,
        loop: true,
        initialSlide: 1
      },
    };
  },

  components: {
    Swiper,
    SwiperSlide,
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.$swiper;
    },
    ...mapState({
      leaders: state => state.leadersInfo.leaders,
    }),
  },
  directives: {
    swiper: directive,
  },
  mounted() {
    this.swiper.slideTo(2, 1000, false);
  },
};
</script>

<style lang="scss" scope>
@import '../scss/variables';
.leaders {
  background-color: #f2f4f9;
  padding-bottom: 80px;
  position: relative;

  .link-to-all{
    display: block;
    margin: auto;
    margin-top: 50px;
  }

  .ellipse {
    position: absolute;
    top: -30%;
    left: 0%;
  }
  .dots {
    position: absolute;
    left: 0;
    top: -20%;
  }
  .title {
    h3 {
      font-weight: bold;
      font-size: 55px;
    }
    .green {
      height: 8px;
      background-color: $base-green;

    }
  }

  .human {
    position: relative;
    cursor: pointer;
    margin-top: 60px;
    .green-filter {
      display: block;
      position: absolute;
      top: 0;
      left: 15px;
      width: calc(100% - 30px);
      content: '';
      height: 100%;
      background: linear-gradient(
        180deg,
        rgba(73, 147, 80, 0) 0%,
        #499350 100%
      );
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .info {
      position: absolute;
      bottom: 10px;
      left: 30px;
      opacity: 0;
      transition: opacity 0.3s ease;
      span {
        font-weight: bold;
        font-size: 24px;
        color: #fff;
      }
      a {
        display: block;
        background: #fff;
        color: #2f80ed;
        font-weight: 500;
        font-size: 16px;
        padding: 4px 8px;
      }
      .audit {
        margin-top: 8px;
        span {
          font-style: normal;
          font-weight: bold;
          font-size: 16px;
          color: #fff;
          margin-left: 12px;
        }
      }
    }
    &:hover {
      .info,
      .green-filter {
        opacity: 1;
        transition: opacity 0.3s ease;
      }
    }
  }

  a {
    &:hover {
      text-decoration: none;
    }
  }

  button {
    width: 234px;
    height: 64px;
    background-color: $base-green;
    color: #fff;
    border-radius: 10px;
    margin: auto;
    margin-top: 48px;
    transition: color 0.3s ease;
    cursor: pointer;
    z-index: 3;
    &:hover {
      background-color: darken($color: $base-green, $amount: 10);
      transition: color 0.3s ease;
    }
  }
}

@media (max-width: 1550px) {
  .leaders {
    .dots {
      width: 100%;
    }
  }
}

@media (max-width: 576px) {
  .leaders .human .green-filter {
    left: 0;
  }

  .leaders {
    .ellipse {
      top: -8%;
    }
    .title {
      h3 {
        font-size: 32px;
      }
      .green {
        height: 4px;
      }
    }
  }
}
</style>
