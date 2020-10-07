<template>
  <div class="running-line d-flex align-items-center justify-content-end">
    <div class="wrapper w-100 justify-content-end d-flex align-items-center">
      <p class="line__p" v-for="Info in Information" :key="Info.general">
        {{ Info.general }}
        <span>{{ Info.amount }}</span>
      </p>
    </div>
  </div>
</template>

<script>
import anime from "animejs/lib/anime.es.js";

export default {
  name: "RunningLine",

  directives: {
    anime
  },

  data() {
    return {
      Information: [
        {
          general: "Общие показы",
          amount: "21.537"
        },
        {
          general: "Инфлюесеров посетило",
          amount: "21.537"
        },
        {
          general: "Аудитория соц сетей",
          amount: "21.537"
        }
      ]
    };
  },
  mounted() {
    anime({
      targets: ".line__p",
      translateX: ["50em", "-100em"],
      duration: 12800,
      easing: "linear",
      loop: true
    });
  }
};
</script>

<style lang='scss'>
.running-line {
  height: 10vh;
  overflow: hidden;

  p {
    margin-right: 16px;
    margin-bottom: 0;
    span {
      color: #219653;
    }
    &:nth-child(2n) {
      span {
        color: #2f80ed;
      }
    }
    &:nth-child(3n) {
      span {
        color: #9b51e0;
      }
    }
  }
}
</style>