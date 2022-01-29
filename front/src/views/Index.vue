<template>
  <v-layout wrap justify-center fill-height class="mx-3">
    <v-card class="pa-4">
      <v-layout wrap justify-center>
        <img src="@/assets/logo.png" alt="osu!Random Tournament Logo">
      </v-layout>
      <v-layout justify-center class="mt-4">
        <h1>Principe</h1>
      </v-layout>
      <v-card-text class="text-xs-center subheading my-4">
        Envie d’un tournoi en team mais sans en choisir ses coéquipiers ? L’osu! Random Tournament est pour vous ! L’osu! Random Tournament (ou o!RT) est un tournoi en team de 4 joueurs se jouant en osu!Standard, ouvert aux joueurs classés entre #1k et #50k. La particularité de ce tournoi réside dans la répartition des joueurs : aucun ne choisira sa team. Ce sera à la place un algorithme optimisé qui fera ce choix et vous placera dans l’une des 16 teams que ce tournoi accueillera, ce qui fait une capacité maximale de 64 participants.
      </v-card-text>
      <v-layout wrap justify-center class="mb-4">
        <router-link to="/reglement"><img src="@/assets/reglement.png" alt="Règlement"></router-link>
        <router-link to="/inscription"><img src="@/assets/inscription.png" alt="Inscription"></router-link>
      </v-layout>
    </v-card>
  </v-layout>
</template>

<script>
  export default {
    name: 'Index'
  }
</script>
