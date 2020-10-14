<template>
  <div class="header d-flex container-xl align-items-center">
    <div class="w-100 d-flex justify-content-between">
      <div class="social d-flex justify-content-between">
        <a v-for="link in links" :key="link.title" v-bind:href="link.url">
          <img :src="link.icon" alt="" />
        </a>
      </div>

      <div class="burger">
        <img src="../assets/burger.svg" alt="" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      links: [
        {
          title: "facebook",
          icon: require("../assets/facebook.svg"),
          url: "#"
        },
        {
          title: "instagram",
          icon: require("../assets/Instagram.svg"),
          url: "#"
        },
          {
          title: "youtube",
          icon: require("../assets/medium.svg"),
          url: "#"
        }
      ]
    };
  }
};
</script>

<style lang="scss">
.header {
  height: 10vh;
}

.social {
  width: 5%;
}
.social>a{
  margin-right: 30px;
}
.burger {
  cursor: pointer;
}

@media (max-width: 1200px){
  .social{
    width: 7%;
  }
}

@media (max-width: 768px){
  .header{
    height: 15vh;
  }
}

@media (max-width: 576px){
  .social{
    width: 20%;
  }
}

</style>