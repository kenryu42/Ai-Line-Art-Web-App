<template>
  <div class="select-none">
    <div
      class="inline-block justify-center cursor-pointer"
      title="Dark Mode"
      aria-label="Dark Mode"
      @click="darkMode"
    >
      <MonoLogo v-show="!dark" />
      <ColorLogo v-show="dark" />
    </div>
    <div
      class="font-serif pt-2 font-bold text-gray-900 dark:text-gray-400 text-xl sm:text-3xl mx-2"
    >
      {{ $t('instruction') }}
    </div>
    <div class="mx-4 pb-6 text-gray-900 dark:text-gray-400">
      <i class="fa fa-info-circle" aria-hidden="true"></i>
      {{ $t('info') }}
    </div>

    <input
      style="display: none"
      type="file"
      accept="image/*"
      ref="imageInput"
      @change="uploadImage"
    />

    <div class="flex justify-center" v-show="!avatar_source">
      <div
        class="max-w-sm tracking-wider bg-green-500 text-black font-bold flex-1 px-4 py-2 ml-5"
      >
        <i class="fa fa-check-square fa-lg" aria-hidden="true"></i>
        {{ $t('ok') }}
      </div>
      <div
        class="max-w-sm tracking-wider bg-red-500 text-black font-bold flex-1 px-4 py-2 mr-5"
      >
        <i class="fa fa-window-close fa-lg" aria-hidden="true"></i>
        {{ $t('ng') }}
      </div>
    </div>
    <div class="flex justify-center items-center" v-show="!avatar_source">
      <div class="ml-4 py-2">
        <img src="/instructions/ok.jpg" alt="OK Image" />
      </div>
      <div class="mr-4 py-2">
        <img :src="ng_photo" alt="NG Image" />
      </div>
    </div>

    <img
      :src="avatar_source"
      v-show="avatar_source"
      alt="Upload Image"
      class="px-2 mx-auto mt-5 h-72"
    />
    <br />
    <button
      :class="[loading_source ? 'cursor-wait' : '']"
      class="font-serif tracking-widest focus:outline-none bg-blue-200 hover:bg-blue-100 dark:bg-green-700 dark:hover:bg-green-600 font-bold text-black py-3 px-8 rounded-full shadow-xl"
      @click="$refs.imageInput.click()"
    >
      {{ $t('upload_button') }}
      <ButtonLogo :class="[loading_source ? 'animate-spin' : '']" />
    </button>
    <div class="my-5 mx-3 dark:text-gray-400">
      <i class="fa fa-user-secret" aria-hidden="true"></i>
      {{ $t('privacy_info') }}
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { TranslateResult } from 'vue-i18n'

interface Data {
  ng_photo: TranslateResult
  dark: boolean
}

export default Vue.extend({
  name: 'UploadComponent',
  props: {
    uploadImage: {
      type: Function,
      required: true,
    },
    avatar_source: {
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
      ng_photo: this.$t('ng_photo'),
      dark: false,
    }
  },
  methods: {
    darkMode(): void {
      this.dark = !this.dark
      this.dark
        ? document.querySelector('html')!.classList.add('dark')
        : document.querySelector('html')!.classList.remove('dark')
    },
  },
})
</script>

<style></style>
