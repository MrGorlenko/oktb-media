<template>
  <div class="main-wrapper">
    <div class="main ">
      <div class="w-100 main__wrap container-xl d-flex justify-content-center flex-column">
        <!-- <div class="main__top container-xl align-items-center"> -->
          <h2 class="main__title">
            Что такое <br />
            "Медиа Будущего"?
          </h2>
        <!-- </div> -->

        <!-- <div class="main__wrapp d-flex container-fluid"> -->
          <div class="container-fluid d-flex justify-content-center">
            <ul class="main__items">
              <li class="main__item" v-for="(item, index) in items" :key="index">
                {{ item.title }}
              </li>
              <button class="btn btn-success " style="margin-left:32px">
                Подробнее
              </button>
            </ul>

            <p class="main__content">
              Приглашение спикеров для <br />
              проведения<b style="color:#66B42F"> мастер-классов</b>, <br />
              организация фестиваля "Точка <br />
              Будущего" раз в год
            </p>
          </div>
        <!-- </div> -->
      </div>
      </div>
  </div>
</template>

<script>
export default {
  name: "MainMedia",
  data() {
    return {
      items: [
        {
          title: "ЛЕКТОРИИ И ФЕСТИВАЛИ"
        },
        {
          title: "УЧИТЕЛЯМ"
        },
        {
          title: "ПРЕСС-СЛУЖБА"
        }
      ]
    };
  }
};
</script>

<style lang="scss" scope>

.main-wrapper{
  background-color: #e5e5e5;
  padding-top: 20vh;
}

.main {
  // background-color: #e5e5e5;
  //background-image: url("~@/assets/Group.svg");
  //  background-color: rgba(255, 255, 255, 0.8);
  // margin-top: 132px;
  background-image: url("~@/assets/backgroundMain.svg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: 0 0;
}
.main__wrap {
  // height: 700px;
  height: 80vh;
  background-image: url("~@/assets/Group.svg");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: 0 0;
}
.main__title {
  // margin-top: 126px;
  margin-bottom: 80px;
  font-family: "San-Francisco", sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 80px;
  line-height: 88px;
  letter-spacing: 2px;
  color: #1c1642;
}
.main__items {
  list-style: none;
  position: relative;
  &::before {
    content: "";
    position: absolute;
    width: 251px;
    height: 0px;
    top: 14px;
    left: -187px;
    width: 251px;
    mix-blend-mode: multiply;
    border: 3px solid #6fcf97;
  }
}
.main__item {
  height: 32px;
  padding-top: 3px;
  width: 276px;
  margin-right: 32px;
  margin-left: 32px;
  margin-bottom: 32px;
  font-family: "San-Francisco", sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 32px;

  color: #000000;
}
.main__content {
  font-family: "San-Francisco", sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 44px;
  line-height: 56px;
  color: #000000;
}
</style>