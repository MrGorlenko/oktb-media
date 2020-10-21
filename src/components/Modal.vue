<template>
  <div class="container d-flex">
    <div class="popup d-flex" ref="popup_p">
      <!-- <div class=" modal-dialog-lg modal-dialog-centered ">-->
      <div class="popup__content pt-3">
        <div class="modal-body d-flex ">
          <div class="ml-3">
            <!-- <slot></slot> -->
            <img class="modal__img" ref="modal__img" :src="leader.img" alt="" />
          </div>
          <div class="ml-3">
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
  height: 150vh;
  background-color: rgba(0, 0, 0, 0.4);
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}

.popup__content {
  //padding: 32px 0px 0px 32px;
  position: absolute;
  width: 918px;
  height: 561px;
  left: 261px;
  top: 10%;
  border-radius: 16px;
  background-color: #ffffff;
  //background-color: #e7e7e7;
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
  right: 15px;
  bottom: 15px;
  //background: rgba(55, 63, 65, 1);
  //color: #ffffff;
  //font-family: Inter;
  //font-size: 18px;
  //font-style: normal;
  //font-weight: 600;
  //line-height: 27px;
  letter-spacing: 0.02em;
  //text-align: left;
}
</style>
