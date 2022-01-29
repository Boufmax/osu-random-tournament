<template>
  <v-card
    :class="`team-card ${ toggleTeam ? 'minimized' : '' }`"
    @click="toggleTeam = !toggleTeam"
  >

    <v-card-title>
      <v-layout row justify-space-between align-center>
        <h3>{{ team.team_name }}</h3>
        <div>
          <span class="team-score">Total score : <b>{{ team.qualifier_score }}</b></span>

          <v-icon
            color="#FFF"
            :class="{ rotate: toggleTeam }"
          >
            keyboard_arrow_down
          </v-icon>
        </div>
      </v-layout>
    </v-card-title>

    <v-card-text class="team-players">
      <v-layout row wrap>

        <TeamPlayer
          v-for="player in team.players"
          :key="player.osu_id"
          :player="player"
        />

      </v-layout>
    </v-card-text>

  </v-card>
</template>

<script>
import TeamPlayer from './TeamPlayer'

export default {
  name: 'TeamCard',
  components: {
    TeamPlayer
  },
  props: {
    team: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      toggleTeam: false
    }
  }
}
</script>

<style scoped>

  .team-card {
    margin: 36px 0;
  }

  .team-card.minimized .team-players {
    max-height: 0;
    padding: 0;
  }

  .team-players {
    max-height: 1000px;
    padding: 32px 16px 12px 16px;
    transition: max-height 0.2s, padding 0.4s;
    overflow: hidden;
  }

  .team-score {
    margin-right: 20px;
  }

  .flex-gap {
    padding: 0 20px;
  }

  .v-card {
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
  }

  .v-card__title {
    cursor: pointer;
    background-color: black;
    color: white;
    font-size: 18px;
    padding: 16px 30px;
  }

  .v-icon {
    transition: transform 0.2s;
    user-select: none;
  }

  .v-icon.rotate {
    transform: rotate(-180deg);
  }

  @keyframes minimized {
    from {
      max-height: 2000px;
      padding: 0 20px;
    }

    to {
      max-height: 0px;
      padding: 0;
    }
  }

</style>
