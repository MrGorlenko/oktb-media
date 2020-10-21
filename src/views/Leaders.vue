<template>
  <div class="leaders_page" id="app">
    <Modal :leader="leader" v-if="modalShow" @closeModal="closeMod" />

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
            <div class="w-100">
              <button
                v-for="(category, index) in leadersCategories"
                :key="category.type"
                v-bind:class="{ active: index == 0 }"
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
              v-for="(category, index) in leadersCategories"
              :key="category.type"
              class="d-none w-100 cat"
              v-bind:class="{ 'd-flex': index == 0 }"
            >
              <div v-for="leader in leaders" :key="leader.name">
                <div
                  class="human w-100"
                  @click="openModal(leader)"
                  v-if="leader.category == category.type"
                >
                  <img style="width:95%;" v-bind:src="leader.img" alt="" />
                  <div style="width:95%; left:0;" class="green-filter "></div>
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
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Modal from '@/components/Modal';
import $ from 'jquery';
import { mapState } from 'vuex';
export default {
  name: 'Leaders',
  data() {
    return {
      leader: {},
      modalShow: false,
      activeIndex: -1,
    };
  },

  components: {
    Modal,
  },
  methods: {
    openModal(leader) {
      this.modalShow = !this.modalShow;
      this.leader = leader;
      //console.log(this.leader);
    },
    closeMod() {
      this.modalShow = false;
    },
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
  computed: {
    ...mapState({
      leadersCategories: state => state.leadersInfo.categories,
      leaders: state => state.leadersInfo.leaders,
    }),
  },

  mounted() {
    // console.log(this.leadersCategories.length)
    let len = this.leadersCategories.length;
    $('.select button').each(function(index) {
      $(this).click(function() {
        $(this).addClass('active');
        $(this)
          .siblings()
          .removeClass('active');
        $(this)
          .parent()
          .parent()
          .parent()
          .parent()
          .children('.col-9')
          .children('.row')
          .children('.cat')
          .eq(index)
          .removeClass('d-none')
          .addClass('d-flex');
        for (let j = 1; j < len; j++) {
          $(this)
            .parent()
            .parent()
            .parent()
            .parent()
            .children('.col-9')
            .children('.row')
            .children('.cat')
            .eq(index + j)
            .removeClass('d-flex')
            .addClass('d-none');
          $(this)
            .parent()
            .parent()
            .parent()
            .parent()
            .children('.col-9')
            .children('.row')
            .children('.cat')
            .eq(index - j)
            .removeClass('d-flex')
            .addClass('d-none');
        }
      });
    });
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

.human {
  position: relative;
  cursor: pointer;
  margin-bottom: 60px;
  .green-filter {
    display: block;
    position: absolute;
    top: 0;
    left: 15px;
    width: calc(100% - 30px);
    content: '';
    height: 100%;
    background: linear-gradient(180deg, rgba(73, 147, 80, 0) 0%, #499350 100%);
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
</style>
