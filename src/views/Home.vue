<template>
  <div class="home">
    <Hero />
    <RunningLine />
    <MainMedia />
    <News-main />
    <Articles />
    <Video />
    <Leaders />
  </div>
</template>

<script>
import Hero from '@/sections/Hero'
import RunningLine from '@/components/RunningLine.vue';
import MainMedia from '@/sections/MainMedia';
import NewsMain from '@/sections/News-main';
import Articles from '@/sections/Articles';
import Video from '@/sections/Video';
import Leaders from '@/sections/Leaders'

export default {
  name: 'Home',
  components: {
    Hero,
    RunningLine,
    MainMedia,
    NewsMain,
    Articles,
    Video,
    Leaders,
  },
};
</script>
