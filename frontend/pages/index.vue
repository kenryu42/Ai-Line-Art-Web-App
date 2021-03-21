<template>
  <div class="v_container dark:bg-gray-900">
    <h2
      class="select-none pt-10 mx-2 my-8 text-2xl font-bold text-gray-800 dark:text-gray-400 md:text-4xl"
    >
      {{ $t('title') }}
    </h2>

    <PortraitSlider />

    <div class="p-6">
      <button
        class="bg-red-600 dark:bg-red-700 focus:outline-none py-3 px-5 mb-40 rounded transform font-bold text-white transition ease-in-out duration-500 shadow-lg hover:scale-125 hover:font-black hover:text-black hover:-translate-y-1"
        @click="moveToStep1"
      >
        {{ $t('button') }}
      </button>
    </div>

    <UploadComponent
      :uploadImage="onFileSelected"
      :avatar_source="avatar"
      :loading_source="loading"
      id="step_1"
    />

    <span
      class="pt-64 animate-pulse m-8 text-2xl dark:text-gray-400 tracking-widest font-semibold"
      v-show="loading"
    >
      {{ loading_message }}
    </span>
    <div class="pb-64">
      <LoadingAnime v-show="loading" />
      <ResultCard
        v-show="result && !loading"
        :loading_source="loading"
        :result_source="result"
        :crop_source="crop"
        :dynamicUrl="dynamicLink"
        class="pt-64"
      />
      <!-- v-show="result && !loading" -->
    </div>
    <div id="step_2"></div>
    <AlertPopup v-show="showAlert" />
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
import jump from 'jump.js'
import { TranslateResult } from 'vue-i18n'

interface Data {
  showAlert: boolean
  loading: boolean
  crop: string
  image: File | FileList | null
  timer: any
  result: string
  avatar: string | ArrayBuffer | null
  dynamicLink: string
  loading_message: TranslateResult
  api: string
}

interface HTMLInputEvent extends Event {
  target: HTMLInputElement & EventTarget
}

export default Vue.extend({
  data(): Data {
    return {
      showAlert: false,
      loading: false,
      crop: '',
      image: null,
      timer: null,
      result: '',
      avatar: '',
      dynamicLink: '',
      loading_message: '',
      api: 'http://0.0.0.0:8080/',
    }
  },
  methods: {
    onFileSelected(event: HTMLInputEvent): void {
      this.image = event.target.files![0]
      let reader: FileReader = new FileReader()
      if (this.image) {
        this.startLoading(event)
        reader.readAsDataURL(this.image)
        reader.onloadend = (e) => {
          this.avatar = e.target!.result
          this.callBackend(event)
        }
      }
    },
    startLoading(event: HTMLInputEvent): void {
      event.target.disabled = true
      this.loading = true
      this.loading_message = this.$t('loading_msg1')
      this.timer = setTimeout(() => {
        this.loading_message = this.$t('loading_msg2')
        setTimeout(() => {
          this.loading_message = this.$t('loading_msg3')
        }, 10000)
      }, 5000)
      setTimeout(this.moveToStep2(), 1000)
      // this.moveToStep2();
    },
    stopLoading(event: HTMLInputEvent): void {
      event.target.disabled = false
      this.loading = false
    },
    moveToStep1(): void {
      const target = document.querySelector('#step_1')
      jump(target!)
    },
    moveToStep2(): any {
      const target = document.querySelector('#step_2')
      jump(target!, {
        duration: 2500,
      })
    },
    callBackend(event: HTMLInputEvent): void {
      const resp = axios
        .post(this.api, {
          image: this.avatar,
        })
        .then((resp) => {
          this.result = resp.data.result
          this.crop = resp.data.crop
          this.stopLoading(event)
        })
        .catch((err) => {
          this.stopLoading(event)
          clearTimeout(this.timer)
          this.showAlert = true
          this.$modal.show('alertModal')
        })
    },
  },
})
</script>

<style>
.v_container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}
</style>
