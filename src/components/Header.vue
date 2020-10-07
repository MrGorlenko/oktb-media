<template>
  <div class="header d-flex container-xl align-items-center">
    <div class="w-100 row justify-content-between">
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

.burger {
  cursor: pointer;
}
</style>