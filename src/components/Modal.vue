<template>
  <div class="container d-flex">
    <div class="popup d-flex align-items-center justify-content-center" ref="popup_p">
      <!-- <div class=" modal-dialog-lg modal-dialog-centered ">-->
      <div class="popup__content pt-3">
        <div class="modal-body d-flex flex-wrap">
          <div class=" col-lg-6 col-12">
            <!-- <slot></slot> -->
            <img class="modal__img" ref="modal__img" :src="leader.img" alt="" />
          </div>
          <div class=" col-lg-6 col-12 p-lg-0">
            <h2 class="modal__title">{{ leader.name }}</h2>
            <p class="modal__job">{{ leader.job }}</p>
            <p class="modal__contact"><b> Телефон: </b> {{ leader.phone }}</p>
            <p class="modal__contact"><b> E-mail: </b> {{ leader.mail }}</p>

            <button class="btn btn-secondary" @click="closeModal">
              Закрыть
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
  name: 'Modal',
  data() {
    return {
      //  modalShow: true,
      activeIndex: -1,
    };
  },
  props: {
    popTitle: {
      type: String,
      default: 'popName',
    },
    leader: {},
  },
  methods: {
    closeModal() {
      this.$emit('closeModal');
      //this.modalShow = !this.modalShow;
    },
  },
  mounted() {
    let vm = this;
    document.addEventListener('click', function(item) {
      if (item.target === vm.$refs['popup_p']) {
        vm.closeModal();
        //console.log(123);
      }
    });
  },
  computed: {
    ...mapState({
      leadersCategories: state => state.leadersInfo.categories,
      leaders: state => state.leadersInfo.leaders,
    }),
  },
};
</script>

<style lang="scss" scoped>
@import '../scss/variables';

.modal__img {
  height: 497px;
  width: 371px;
}

.popup {
  z-index: 100;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.popup__content {

  width: 918px;
  height: 561px;
  border-radius: 16px;
  background-color: #ffffff;
  &__job {
    font-weight: normal;
    font-size: 27px;
    line-height: 150%;
    color: #272b2d;
  }
  &__contact {
    font-weight: 400;
    font-size: 18px;
    line-height: 150%;
    color: #272b2d;
  }
}

.modal__title {
  font-style: normal;
  font-weight: bold;
  font-size: 44px;
  line-height: 120%;
  /* or 53px */

  letter-spacing: 0.01em;

  /* #272B2D */

  color: #272b2d;
}
.btn {
  position: absolute;
  right: 35px;
  bottom: 15px;
  letter-spacing: 0.02em;
  //text-align: left;
}

@media (max-width: 992px){
  .popup{
    height: 102vh;
    h2, p{
      text-align: center;
    }
  }
  .popup__content{
    width: 100%;
    height: 100%;
    overflow: scroll;
    border-radius: 0px;
  }
  .modal-body{
    height: 100%;
    padding-top: 0;
  }
  .btn{
    position: relative;
    margin: auto;
    display: block;
    right:0;
    margin-top: 25px;
  }
  .modal__img{
    margin:auto;
    display: block;
    width: 100%;
    height: auto;
  }
}
</style>
