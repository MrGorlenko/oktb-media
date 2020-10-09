<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Header />
    <Hero />
    <RunningLine />
    <MainMedia />
    <News-main />
    <Articles />
    <Leaders />
  </div>
</template>

<script>
import Header from '@/components/Header';
import Hero from '@/sections/Hero'
import RunningLine from '@/components/RunningLine.vue';
import MainMedia from '@/sections/MainMedia';
import NewsMain from '@/sections/News-main';
import Articles from '@/sections/Articles';
import Leaders from '@/sections/Leaders'

export default {
  name: 'Home',
  components: {
    Header,
    Hero,
    RunningLine,
    MainMedia,
    NewsMain,
    Articles,
    Leaders
  },
};
</script>
