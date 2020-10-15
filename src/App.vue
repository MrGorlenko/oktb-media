<template>
  <div id="app">
<!--   <Home />
 -->  
  <router-view/> 
  </div>
</template>
<script>
/* import Home from '@/views/Home'
 */
 /* export default {
  
} */
</script>

<style lang="scss">

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

a:hover{
  text-decoration: none;
}

button{
  border: none;
  cursor: pointer;
  outline: none !important;
}

.w-48{
  width: 48%;
}

.w-90{
  width: 90%;
}

.w-98{
  width: 98%;
}

@media (min-width: 1200px){
  .container-xl{
    max-width: 1440px !important;
  }
}

@media (min-width: 992px){
  .w-lg-100{
    width: 100% !important;
  }
  .w-lg-48{
    width: 48% !important;
  }
  .h-lg-100{
    height: 100% !important;
  }
  .col-lg-5-8{
    flex: 0 0 48% !important;
    max-width: 48% !important;
  }
}

@media (max-width: 992px) {
  .w-mob-100{
    width: 100% !important; 
  }
  .w-mob-98{
    width: 98% !important;
  }
}
</style>
