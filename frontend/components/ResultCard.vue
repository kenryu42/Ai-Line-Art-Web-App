<template>
  <div>
    <div
      class="max-w-xs bg-gray-200 dark:bg-gray-800 rounded overflow-hidden shadow-2xl"
    >
      <div class="relative w-80 h-80">
        <img
          class="absolute w-80 h-80"
          :src="crop_source"
          alt="cropped_image"
        />
        <img
          class="absolute"
          :src="result_source"
          ref="top"
          alt="result_image"
        />
      </div>
      <div class="px-6 py-2 text-gray-800 dark:text-blue-300">
        <div class="font-bold text-gray-800 dark:text-gray-300 text-xl my-6">
          {{ $t('share_sns') }}
        </div>
        <div class="flex justify-center">
          <ShareNetwork
            class="cursor-pointer"
            network="facebook"
            :url="dynamicUrl"
            title="I just had my line drawing portrait with AI Line Art!"
            description="AI Line Art generates line drawing portrait from your photo"
            quote="The line has almost become a work of art in itself. -  Theo van Doesburg"
            hashtags="ailineart"
          >
            <FacebookIcon />
          </ShareNetwork>
          <div class="px-6"></div>
          <ShareNetwork
            class="cursor-pointer"
            network="twitter"
            :url="dynamicUrl"
            :title="sn_title"
            :description="sn_description"
            hashtags="ailineart"
          >
            <TwitterIcon />
          </ShareNetwork>
          <div class="px-6"></div>
          <ShareNetwork
            class="cursor-pointer"
            network="whatsapp"
            :url="dynamicUrl"
            title="I just had my line drawing portrait with AI Line Art!"
            description="AI Line Art generates line drawing portrait from your photo"
            quote="The line has almost become a work of art in itself. -  Theo van Doesburg"
            hashtags="ailineart"
          >
            <WhatsappIcon />
          </ShareNetwork>
        </div>
        <div class="mt-10 flex justify-center">
          <ShareNetwork
            class="cursor-pointer"
            network="weibo"
            :url="dynamicUrl"
            title="I just had my line drawing portrait with AI Line Art!"
            description="AI Line Art generates line drawing portrait from your photo"
            quote="The line has almost become a work of art in itself. -  Theo van Doesburg"
            hashtags="ailineart"
          >
            <WeiboIcon />
          </ShareNetwork>
          <div class="px-7"></div>
          <ShareNetwork
            class="cursor-pointer"
            network="vk"
            :url="dynamicUrl"
            title="I just had my line drawing portrait with AI Line Art!"
            description="AI Line Art generates line drawing portrait from your photo"
            quote="The line has almost become a work of art in itself. -  Theo van Doesburg"
            hashtags="ailineart"
          >
            <VkIcon />
          </ShareNetwork>
        </div>
      </div>
      <div class="px-6 py-4">
        <button
          type="button"
          @click="switchImage"
          class="inline-block focus:outline-none"
        >
          <On v-show="!show" />
          <Off v-show="show" />
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { TranslateResult } from 'vue-i18n'

interface Data {
  show: boolean
  sn_title: TranslateResult
  sn_description: TranslateResult
}

export default Vue.extend({
  name: 'ResultCard',
  props: {
    result_source: {
      type: String,
      required: true,
    },
    crop_source: {
      type: String,
      required: true,
    },
    dynamicUrl: {
      type: String,
      required: true,
    },
    loading_source: {
      type: Boolean,
      required: true,
    },
  },
  data(): Data {
    return {
      show: false,
      sn_title: this.$t('sn_title'),
      sn_description: this.$t('sn_description'),
    }
  },
  methods: {
    switchImage(): void {
      ;(this.$refs.top as any).style.opacity ^= 1
      this.show = !this.show
    },
  },
  watch: {
    loading_source(): void {
      ;(this.$refs.top as any).style.opacity = 1
      this.show = false
    },
  },
  mounted() {
    ;(this.$refs.top as any).style.opacity = 1
  },
})
</script>

<style scoped>
img {
  opacity: 1;
  -webkit-transition: opacity 1s ease-in-out;
  -moz-transition: opacity 1s ease-in-out;
  -o-transition: opacity 1s ease-in-out;
  transition: opacity 1s ease-in-out;
}
</style>
