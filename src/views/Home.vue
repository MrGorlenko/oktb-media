<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Header />
    <Hero />
    <RunningLine />
    <MainMedia />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Header from "@/components/Header.vue";
import Hero from "@/components/Hero.vue";
import RunningLine from "@/components/RunningLine.vue";
import MainMedia from "@/components/MainMedia";

export default {
  name: "Home",
  components: {
    Header,
    Hero,
    RunningLine,
    MainMedia
  }
};
</script>
