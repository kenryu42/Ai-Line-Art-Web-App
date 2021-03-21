<template>
  <modal name="alertModal">
    <div
      class="flex flex-col text-black text-center justify-center items-center"
      v-show="show"
    >
      <Sorry />{{ $t('alert') }}
      <div class="mt-8">
        <button
          class="font-bold bg-black text-white rounded-full py-2 px-8"
          @click="$modal.hide('alertModal')"
        >
          Close
        </button>
      </div>
    </div>
  </modal>
</template>
<script>
export default {
  name: 'AlertPopup',
  props: ['show'],
  methods: {
    closeModal() {
      this.$modal.hide('alertModal')
      props.show = false
    },
  },
}
</script>
