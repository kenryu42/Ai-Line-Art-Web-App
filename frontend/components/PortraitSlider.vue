<template>
  <!-- Swiper -->
  <div class="m-2 swiper-container w-full pt-3">
    <div class="swiper-wrapper">
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider1.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider2.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider3.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider4.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider5.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider6.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider7.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider8.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider9.png)"
      ></div>
      <div
        class="swiper-slide"
        style="background-image: url(/slider/slider10.png)"
      ></div>
    </div>
    <!-- Add Pagination -->
    <!-- <div class="swiper-pagination"></div> -->
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import Swiper from 'swiper'

export default Vue.extend({
  name: 'PortraitSlider',
  mounted() {
    const swiper: Swiper = new Swiper('.swiper-container', {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 'auto',
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
      coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
      },
    })
  },
})
</script>

<style>
.swiper-slide {
  width: 356px;
  height: 356px;
}
</style>
