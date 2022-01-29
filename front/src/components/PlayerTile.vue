<template>
  <v-list-tile v-ripple avatar :href="`https://osu.ppy.sh/users/${player.osu_id}`" target="_blank">
    <v-list-tile-avatar>
      <img :src="`https://a.ppy.sh/${player.osu_id}`">
    </v-list-tile-avatar>

    <v-list-tile-content>
      <v-list-tile-title class="font-weight-bold">{{ player.username }}</v-list-tile-title>
      <v-list-tile-sub-title>{{ player.pp }} pp</v-list-tile-sub-title>
    </v-list-tile-content>

    <v-list-tile-action>
      <v-chip outline :color="color">#{{ rank }}</v-chip>
    </v-list-tile-action>
  </v-list-tile>
</template>

<script>
import formatRank from '../utils/formatRank'

export default {
  name: 'PlayerTile',
  props: {
    player: {
      type: Object,
      required: true
    }
  },
  computed: {
    rank () {
      return formatRank(this.player.rank)
    },
    color () {
      if (this.player.rank >= 50000) return 'grey'
      if (this.player.rank >= 25000) return 'black'
      if (this.player.rank >= 10000) return 'primary'
      if (this.player.rank > 1000) return 'pink'
      if (this.player.rank <= 1000) return 'amber darken-2'
      return 'grey'
    }
  }
}
</script>

<style>

  .v-avatar img {
    border: 1px solid rgba(0, 0, 0 , 0.2)
  }

</style>
