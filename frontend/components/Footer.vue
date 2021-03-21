<template>
  <footer
    class="flex justify-center select-none px-4 bg-gray-900 dark:bg-gray-800"
  >
    <div class="container py-6">
      <span class="flex justify-center items-center">
        <a
          class="text-lg font-bold lg:text-2xl text-gray-300 hover:text-red-600"
          href="https://github.com/yiranran/Unpaired-Portrait-Drawing"
          rel="noopener noreferrer"
          target="_blank"
          >#{{ $t('credit') }}</a
        >
      </span>

      <hr class="h-px m-6 bg-gray-700 border-none" />
      <div class="flex justify-around">
        <ShareNetwork
          class="cursor-pointer"
          network="twitter"
          url="https://ailineart.com"
          title="Create your line art portrait with AI Line Art."
          hashtags="ailineart"
        >
          <TwitterShare />
        </ShareNetwork>
        <ShareNetwork
          class="cursor-pointer"
          network="whatsapp"
          url="https://ailineart.com"
          title="Create your line art portrait with AI Line Art."
        >
          <WhatsappShare />
        </ShareNetwork>
        <ShareNetwork
          class="cursor-pointer"
          network="facebook"
          url="https://ailineart.com"
          title="Create your line art portrait with AI Line Art."
          quote="The line has almost become a work of art in itself. - Theo van Doesburg"
          hashtags="ailineart"
        >
          <FacebookShare />
        </ShareNetwork>
      </div>

      <hr class="h-px m-6 bg-gray-700 border-none" />

      <div class="text-center">
        <div class="flex items-center justify-center text-gray-500">
          Made with <Love /> by
          <a
            class="hover:text-red-600 ml-1"
            href="https://liewjenglung.com/"
            title="My website"
            aria-label="My website"
            rel="noopener noreferrer"
            target="_blank"
            >liewjenglung.com</a
          >
        </div>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  name: 'FooterComp',
}
</script>
