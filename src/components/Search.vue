<template>
    <div class="search container-xl align-items-center">
        <div class="container d-flex flex-column justify-content-between ">
            <h2 class="search__news mb-4">Новости</h2>
        <div class="input__wrap w-100">
            <input class="input__news w-100"
            type="text" placeholder="Поиск">
        </div>
        <ul class="items__hash d-flex col-lg-6 justify-content-between p-0 mt-1">
            <li class="item__hash">#хэштег</li>
            <li class="item__hash">#хэштег</li>
            <li class="item__hash">#хэштег</li>
            <li class="item__hash">#хэштег</li>
            <li class="item__hash">#хэштег</li>
            <li class="item__hash">#хэштег</li>

        </ul> 
        
    </div>
    </div>
</template>

<script>
export default {
    name:"Search"
}
</script>

<style lang="scss">
@import '../scss/variables';
.search{
    font-family: $base-family;
}
.search__news{
    font-family: $base-family;
    font-style: normal;
    font-weight: bold;
    font-size: 80px;
    line-height: 88px;
    margin-top: 56px;
    margin-bottom: 45px;
    }
.input__news{
    height: 60px;
    border: none;
    padding: 20px;
    padding-left: 50px;
}
.input__wrap{
    position: relative;
      &::before{
        content:'';
        position: absolute;
        top: 17px;
        left: 15px; 
        background-image: url('~@/assets/search.svg');
        background-repeat: no-repeat;
        background-position: 0 0;
        width: 24px;
        height: 24px;
    }
}
.items__hash{
    list-style: none;
}
.item__hash{
    padding: 0px;
    padding-left: 0px;
    color: rgba(28, 22, 66, 1);
    width: 77px;
    border-right: 1px solid $grey-news;
     &:hover{
        cursor: pointer;
        border-bottom: 2px solid $base-green;
    }
}
.input__hash{
    font-weight: 500;
    font-size: 19px;
    line-height: 24px;
}

@media (max-width: 376px) {
    .search{
    background-color: $base-bg-news;
}
    .search__news{
    font-weight: bold;
    font-size: 50px;
    line-height: 56px;
    letter-spacing: 2px;
    margin: 0 auto;
    margin-top: 24px;
    margin-bottom: 25px;
    }
}
</style>