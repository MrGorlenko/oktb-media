<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Header />
    <Hero />
    <RunningLine />
    <MainMedia />
    <News-main />
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import Hero from "@/components/Hero.vue";
import RunningLine from "@/components/RunningLine.vue";
import MainMedia from "@/components/MainMedia";
import NewsMain from '@/components/News-main'

export default {
  name: "Home",
  components: {
    Header,
    Hero,
    RunningLine,
    MainMedia,
    NewsMain
  }
};
</script>
