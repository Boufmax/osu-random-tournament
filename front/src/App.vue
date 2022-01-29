<template>
  <v-app>
    <Navbar />

    <v-content>
      <v-layout fill-height wrap>
        <v-flex lg8 offset-lg2 xl6 offset-xl3 class="my-5">
          <transition name="slide-y-transition" mode="out-in">
            <router-view/>
          </transition>
        </v-flex>
      </v-layout>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'

export default {
  name: 'App',
  components: {
    Navbar,
    Footer
  }
}
</script>

<style>

  html {
    overflow-y: auto;
  }

  .v-card {
    height: fit-content;
    width: 100%;
  }

  .subheading {
    font-size: 18px !important;
  }

  img {
    user-select: none;
  }

</style>

