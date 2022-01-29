<template>
  <v-layout align-center justify-center column wrap>
    <h1 class="display-2"><code>{{ this.$route.path }}</code> n'existe pas</h1>
    <img src="@/assets/not-found.svg" alt="Undraw.co not found" />
    <v-btn to="/" large color="primary">Accueil</v-btn>
  </v-layout>
</template>

<script>
export default {
  name: 'NotFound'
}
</script>

<style scoped>

  .layout {
    height: 100%;
  }

  img {
    padding: 64px;
    height: 400px;
    width: 100%;
    object-fit: contain;
  }

</style>
