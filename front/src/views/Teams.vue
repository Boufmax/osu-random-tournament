<template>
  <v-layout wrap justify-center fill-height class="mx-3">
    <v-card class="pa-4">
      <v-layout wrap justify-center>
        <img src="@/assets/logo.png" alt="osu!Random Tournament Logo">
      </v-layout>

      <h2 class="text-xs-center display-1 font-weight-bold">Teams</h2>

      <v-layout row wrap>
        <v-flex lg10 offset-lg1 xl8 offset-xl2>
          <v-list two-line>
            <v-layout row justify-space-between align-center>
              <v-subheader>{{ teams.length }} teams</v-subheader>

              <v-subheader class="clickable" @click="sortTeamsByScore">
                Trier par qualifiers score
                <v-icon :class="{ rotate: toggleSort }">
                  keyboard_arrow_up
                </v-icon>
              </v-subheader>
            </v-layout>
          </v-list>

          <v-layout row justify-center>
            <img v-if="!teams.length" class="no-players" src="@/assets/no_players.svg" alt="No players registered yet">
          </v-layout>
        </v-flex>
      </v-layout>

    </v-card>

    <TeamCard
      v-for="team in teams"
      :key="team.team_name"
      :team="team"
    />
  </v-layout>
</template>

<script>
import TeamCard from '../components/TeamCard'

export default {
  name: 'Listing',
  components: {
    TeamCard
  },
  data () {
    return {
      teams: [],
      toggleSort: true // true = desc
    }
  },
  created () {
    this.hydrateTeams()
  },
  methods: {
    async hydrateTeams () {
      const data = await (await fetch('/teams')).json()
      const teams = this.sortTeams(data)
      teams.sort((a, b) => b.qualifier_score - a.qualifier_score)
      this.teams = teams
    },
    sortTeams (teams) {
      const newTeams = []

      teams.forEach(team => {
        /* eslint-disable camelcase */
        const qualifier_score = team.players.reduce((totalScore, player) => totalScore + player.qualifier_score, 0)

        const players = team.players.sort((a, b) => b.qualifier_score - a.qualifier_score)

        newTeams.push({
          team_name: team.team_name,
          players,
          qualifier_score
        })
      })

      return newTeams
    },
    sortTeamsByScore () {
      if (this.toggleSort) {
        // Asc by default
        this.teams.sort((a, b) => a.qualifier_score - b.qualifier_score)
      } else {
        // Desc
        this.teams.sort((a, b) => b.qualifier_score - a.qualifier_score)
      }

      this.toggleSort = !this.toggleSort
    }
  }
}
</script>

<style scoped>

  h2 {
    margin: 32px 0;
  }

  .staff {
    display: inline-block;
    padding: 12px;
    border: 1px solid rgba(0, 0, 0, 0.1);
    border-radius: 8px;
  }

  .v-list {
    width: 100%;
  }

  h2 .v-icon {
    line-height: 34px;
    font-size: 34px;
    transition: transform 0.2s;
    user-select: none;
    cursor: pointer;
  }

  .v-icon.rotate {
    transform: rotate(-180deg);
  }

  .v-subheader .v-icon {
    margin-left: 6px;
  }

  .clickable {
    cursor: pointer;
    user-select: none;
  }

  .clickable .v-icon {
    margin: 0;
  }

  .no-players {
    height: 240px;
    display: block;
    width: 100%;
  }

</style>
