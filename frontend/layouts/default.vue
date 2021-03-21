<template>
  <div>
    <nuxt />
    <Footer />
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: this.$t('meta_title'),
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: this.$t('meta_description'),
        },
        {
          name: 'twitter:title',
          content: this.$t('twitter_title'),
        },
        {
          name: 'twitter:description',
          content: this.$t('twitter_description'),
        },
        {
          hid: 'og:site_name',
          name: 'og:site_name',
          property: 'og:site_name',
          content: this.$t('og_site_name'),
        },
        {
          hid: 'og:title',
          property: 'og:title',
          content: this.$t('og_title'),
        },
        {
          hid: 'og:description',
          property: 'og:description',
          content: this.$t('og_description'),
        },
        {
          hid: 'og:url',
          property: 'og:url',
          content: this.$t('og_url'),
        },
      ],
    }
  },
}
</script>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  -webkit-tap-highlight-color: transparent;
  box-sizing: border-box;
  overflow-x: hidden;
}
</style>
