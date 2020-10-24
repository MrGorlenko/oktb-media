<template>
  <div class="news">
    <div class="container">
      <h2 class="search__news mb-4">Новости</h2>
    </div>
    <router-view></router-view>
    <Search />
    <NewsCard />
  </div>
</template>

<script>
import Search from '@/components/Search';
import NewsCard from '@/components/News-Card';

export default {
  name: 'News',
  components: {
    // Header,
    Search,
    NewsCard,
  },
};
</script>

<style lang="scss" scope>
@import '../scss/variables';
.news {
  background-color: $base-bg-news;
  padding-bottom: 10px;
}

@media (max-width: 376px) {
  .news {
    background-color: #ffffff;
  }
}
</style>
