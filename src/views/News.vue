<template>
  <div class="news">
  <Header />
  <Search />
  </div>
</template>

<script>
import Header from '@/components/Header'
import Search from '@/components/Search'

export default {
  name: 'News',
  components: {
  Header,
  Search
  },
};
</script>

<style lang="scss">
@import '../scss/variables';
  .news{
    background-color: $base-bg-news;
    padding-bottom: 10px;
  }

  @media (max-width: 376px) {
    .news{
        background-color: #ffffff;
    }
}
</style>
