<template>
  <div class="main-wrapper">
    <div class="main ">
      <img class='ellipse' src="../assets/Ellipse.svg" alt="">
      <div
        class="w-100 main__wrap container-xl d-flex justify-content-start justify-content-lg-center flex-column"
      >
      <!-- Group.svg -->
        <img class='dots' src="../assets/Group.svg" alt="">
        <!-- <div class="main__top container-xl align-items-center"> -->
        <h2 class="main__title">
          Что такое <br />
          "Медиа Будущего"?
        </h2>
        <!-- </div> -->

        <!-- <div class="main__wrapp d-flex container-fluid"> -->
        <div class="container-fluid d-flex flex-lg-row flex-column justify-content-center">
          <ul class="main__items d-flex d-sm-block justify-content-between flex-wrap">
            <li class="main__item" v-for="(item, index) in items" :key="index">
              {{ item.title }}
            </li>
            <button class="btn btn-success btn-lg " style="margin-left:32px">
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
  name: 'MainMedia',
  data() {
    return {
      items: [
        {
          title: 'ЛЕКТОРИИ И ФЕСТИВАЛИ',
        },
        {
          title: 'УЧИТЕЛЯМ',
        },
        {
          title: 'ПРЕСС-СЛУЖБА',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scope>
.main-wrapper {
  background-color: #f2f4f9;
  padding-top: 20vh;
}

.main {
  background-image: url('~@/assets/backgroundMain.svg');
  background-size: contain;
  background-repeat: no-repeat;
  background-position: 50% 37%;

  position: relative;
  .ellipse{
    position: absolute;
    top: -5%;
    left: -5%;
  }

  @media screen and (min-width: 1550px){
    background-size: cover;
  }
}
.main__wrap {
  height: 800px;

  position: relative;
  .dots{
    position: absolute;
    width:100%;
    top: 0;
    left: 0;
  }
}
.main__title {
  margin-bottom: 80px;
  font-family: 'San-Francisco', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 80px;
  line-height: 88px;
  letter-spacing: 2px;
  color: #1c1642;
  z-index: 3;
}
.main__items {
  list-style: none;
  position: relative;
   @media(min-width:768px) {
   &::before {
    content: '';
    position: absolute;
    width: 251px;
    height: 0px;
    top: 14px;
    left: -187px;
    width: 251px;
    mix-blend-mode: multiply;
    border: 1px solid #6fcf97;
  }}
}
.main__item {
  height: 32px;
  padding-top: 3px;
  //width: 276px;
  margin-right: 32px;
  margin-left: 32px;
  margin-bottom: 32px;
  font-family: 'San-Francisco', sans-serif;
  font-style: normal;
  font-weight: bold;
  font-size: 18px;
  line-height: 32px;
  color: #000000;
/*   @media(max-width:567px) {
     
    &::before {
    
    content: '';
    position: absolute;
    width: 16px;
    height: 0px;
    top: 14px;
   // width: 251px;
    mix-blend-mode: multiply;
    border: 1px solid #6fcf97;
    } }
     */
  
  &:hover {
    cursor: pointer;
    color: #219653;
  }
   
}
.main__content {
  font-family: 'San-Francisco', sans-serif;
  font-style: normal;
  font-weight: 600;
  font-size: 44px;
  line-height: 56px;
  color: #000000;
}

@media (max-width: 375px) {
  .main{
    background-image: url('~@/assets/backgroundMainES.svg');
    background-size: cover;
    background-position: 50% 37%;
   
  }
  .main-wrapper{
    padding-top: 60px;
  }
  .main__wrap{
    height: 520px;
  }
  .main__title{
  margin-top: 50px;
  margin-bottom: 40px;
font-style: normal;
font-weight: bold;
font-size: 31px;
line-height: 120%;
  }
  .ellipse{
    width: 124px;
    height: 124px;
  }
  .main .ellipse{
    top: -3%;
    left: -9%;
  }
  .main__items{
    //width: 345px;
    padding: 0;
   
  }  
  .main__item{
    display: block;
  padding-top: 0px;
    margin: 0;
font-size: 14px;
line-height: 32px;
  }
  .btn{
    position: relative;
    top: 245px;
    left: -176px;
  }
br{
  display: none;
}
  .main__content{
    font-weight: 600;
font-size: 24px;
line-height: 32px;
  }
  
}
</style>
