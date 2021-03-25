export default {
  target: 'static',
  /*
   ** Headers of the page
   */
  head: {
    title: 'AI Line Art',
    // title: process.env.npm_package_name || "",
    meta: [
      { charset: 'utf-8' },
      {
        name: 'viewport',
        content: 'width=device-width, initial-scale=1',
      },
      {
        hid: 'mobile-web-app-capable',
        name: 'mobile-web-app-capable',
        content: 'yes',
      },
      {
        hid: 'apple-mobile-web-app-title',
        name: 'apple-mobile-web-app-title',
        content: 'AI-Line-Art',
      },
      {
        hid: 'author',
        name: 'author',
        content: 'Kr203',
      },
      {
        hid: 'description',
        name: 'description',
        content:
          'AI generates line art portrait from your photo. One of the most fundamental elements of art is the line. AI Line Art is capable of generate line art portrait for you instantly.',
      },
      {
        name: 'twitter:card',
        content: 'summary_large_image',
      },
      {
        name: 'twitter:site',
        content: '@AiLineArt',
      },
      {
        name: 'twitter:title',
        content: 'AI Line Art',
      },
      {
        name: 'twitter:description',
        content: 'AI generates line art portrait from your photo',
      },
      {
        name: 'twitter:image',
        content: 'https://ailineart.com/ogp-data/ogp-image.jpg',
      },
      {
        hid: 'og:site_name',
        name: 'og:site_name',
        property: 'og:site_name',
        content: 'AI Line Art',
      },
      {
        hid: 'og:type',
        property: 'og:type',
        content: 'website',
      },
      {
        hid: 'og:title',
        property: 'og:title',
        content: 'AI Line Art',
      },
      {
        hid: 'og:description',
        property: 'og:description',
        content: 'AI generates line art portrait from your photo',
      },
      {
        hid: 'og:url',
        property: 'og:url',
        content: 'https://ailineart.com',
      },
      {
        hid: 'og:image',
        property: 'og:image',
        content: 'https://ailineart.com/ogp-data/ogp-image.jpg',
      },
    ],
    link: [
      {
        rel: 'stylesheet',
        href:
          'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
      },
    ],
    script: [{}],
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['swiper/css/swiper.min.css'],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    '~/plugins/anime.js',
    { src: '~/plugins/vue-js-modal', ssr: false },
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/nuxt-tailwindcss
    '@nuxtjs/pwa',
    '@nuxtjs/tailwindcss',
    '@nuxt/typescript-build',
  ],
  /*
   ** Nuxt.js modules
   */
  modules: ['nuxt-i18n', 'vue-social-sharing/nuxt'],
  i18n: {
    strategy: 'prefix_except_default',
    locales: [
      {
        code: 'en',
        iso: 'en_US',
        file: 'en.json',
      },
      {
        code: 'ja',
        iso: 'ja_JP',
        file: 'ja.json',
      },
    ],
    detectBrowserLanguage: {
      // If enabled, a cookie is set once a user has been redirected to his
      // preferred language to prevent subsequent redirections
      // Set to false to redirect every time
      useCookie: true,
      // Cookie name
      cookieKey: 'i18n_redirected',
      onlyOnRoot: true,
      // Set to always redirect to value stored in the cookie, not just once
      alwaysRedirect: true,
      // If no locale for the browsers locale is a match, use this one as a fallback
      // fallbackLocale: "en"
    },
    defaultLocale: 'en',
    lazy: true,
    langDir: 'lang/',
    seo: false,
  },
  pwa: {
    meta: {
      theme_color: '#f9fafb',
    },
  },
  build: {},
  server: {
    host: '0.0.0.0',
  },
  components: ['~/components', '~/components/svg'],
}
