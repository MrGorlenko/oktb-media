<template>
  <div class="home">
    <Header />
    <Hero />
    <RunningLine />
    <MainMedia />
    <News-main />
    <Articles />
    <Video />
    <Leaders />
    <!-- <Footer /> -->
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
import Video from '@/sections/Video';
// import Footer from '@/components/Footer';

export default {
  name: 'Home',
  components: {
    Header,
    Hero,
    RunningLine,
    MainMedia,
    NewsMain,
    Articles,
    Leaders,
    Video,
    // Footer
  },
};
</script>
