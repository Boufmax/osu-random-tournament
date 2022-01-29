<template>
  <v-layout wrap justify-center fill-height class="mx-3">
    <v-card class="pa-4">
      <v-layout wrap justify-center>
        <img src="@/assets/logo.png" alt="osu!Random Tournament Logo">
      </v-layout>
      <v-layout justify-center class="mt-4">
        <h1>Règlement</h1>
      </v-layout>
      <v-card-text class=" subheading my-4">
        
        <ul>
          <li>Concerne les joueurs classés entre les ranks #1 à #50.000.</li>
          <li>Ouvert aux francophones.</li>
          <li>La charte de convivialité osu!, devra évidemment être respectée.</li>
          <li>
              Le <b>ScoreV2</b> sera utilisé pour tous les matchs.
          </li>
          <li>
              À la fin de la période d’inscription, les <b>64 meilleurs joueurs</b> seront retenus 
              (répartis en 16 teams de 4 joueurs).
          </li>
          <li>
              Le seeding se fera à partir de 4 poules de joueurs également réparties :
              high seed, mid seed, low seed et no seed, chaque team sera composée d’un joueur de chaque seed.  
          </li>
          <li>
              Il est prié de prévenir l'équipe du staff en cas de problème : 
              absence ou redéfinition de l'horaire d'un match. Nous traiterons ainsi au mieux cet incident.
          </li>
          <li>
              Un équilibrage des teams sera probablement fait juste avant le tournoi : 
              si des teams se retrouvent à moins de deux joueurs avant même les matchs, 
              il se pourrait que ses joueurs en soient dispatchés dans des teams incomplètes.
          </li>
          <li>
              Il est très <b><u>conseillé</u></b>
              de rejoindre le <a href="https://discord.gg/C3A6A27">Discord</a> de l’évènement, pour ne pas rater les 
              dernières infos mais aussi pour pouvoir rapidement prendre contact si besoin 
              (pseudo IG en accord avec celui sur Discord, pour éviter les confusions).
          </li>
          <li>
              Chaque team aura droit à <b>son channel privé</b> sur Discord afin de s’organiser, 
              cela évitera la création de conversations privées ou de serveurs tiers.
          </li>
          <li>
              N’hésitez pas à nous <b>proposer un nom de team</b> après la répartition des joueurs, 
          </li>
          <li>
              En cas d’un absent dans l’équipe, il sera demandé à l’équipe adverse de ne pas faire jouer son joueur de même seeding. 
              Ainsi, avec maximum deux absents (un par team), le match peut être jusqu'à un 2v2.
          </li>
          <li> En cas de deux absences ou plus, l’équipe concernée sera considérée comme forfaitaire du match.</li>
        </ul>

      </v-card-text>

      <v-layout wrap justify-center class="mb-4">
        <router-link to="/inscription"><img src="@/assets/inscription.png" alt="Inscription"></router-link>
      </v-layout>
    </v-card>
  </v-layout>
</template>

<script>
export default {
  name: 'Rules'
}
</script>

<style scoped>

  ul li {
    margin: 8px 0;
  }

  a {
    color: #29b;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

</style>
