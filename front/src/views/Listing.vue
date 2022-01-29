<template>
  <v-layout wrap justify-center fill-height class="mx-3">
    <v-card class="pa-4">
      <v-layout wrap justify-center>
        <img src="@/assets/logo.png" alt="osu!Random Tournament Logo">
      </v-layout>

        <v-layout justify-center row wrap>
          <v-flex>
            <v-layout row justify-center>
              <h2 @click="toggleStaff" class="staff clickable text-xs-center display-1 font-weight-bold">
              Équipe du staff
              <v-icon :class="{ rotate: isExpanded }" style="line-height: 42px;">keyboard_arrow_down</v-icon>
            </h2>
            </v-layout>
            <transition name="slide-x-transition">
              <div v-if="isExpanded">
                <v-subheader>Organisateurs <v-icon>group</v-icon></v-subheader>
                  <v-layout row wrap>
                    <StaffMember username="Bouf" avatar="https://a.ppy.sh/4431069?1546567528.jpeg"/>
                    <StaffMember username="Ukabi" avatar="https://a.ppy.sh/8661245?1533855258.png"/>
                  </v-layout>
                <v-subheader>Arbitres <v-icon>assignment_ind</v-icon></v-subheader>
                  <v-layout row wrap>
                    <StaffMember username="FayeurS 5" avatar="https://a.ppy.sh/6177263?1547741833.png"/>
                    <StaffMember username="Ryumi" avatar="https://a.ppy.sh/6596270?1543267392.png"/>
                  </v-layout>
                <v-subheader>GFX <v-icon>brush</v-icon></v-subheader>
                  <v-layout row wrap>
                    <StaffMember username="LoTcho"/>
                  </v-layout>
                <v-subheader>Devs <v-icon>code</v-icon></v-subheader>
                  <v-layout row wrap>
                    <StaffMember username="Bouf" avatar="https://a.ppy.sh/4431069?1546567528.jpeg"/>
                    <StaffMember username="Nemesis-" avatar="https://a.ppy.sh/5914915?1543271201.jpeg"/>
                    <StaffMember username="Ukabi" avatar="https://a.ppy.sh/8661245?1533855258.png"/>
                  </v-layout>
                <v-subheader>Host <v-icon>live_tv</v-icon></v-subheader>
                  <v-layout row wrap>
                    <StaffMember username="???"/>
                  </v-layout>
                <v-subheader>Mapsetters <v-icon>code</v-icon></v-subheader>
                  <v-layout row wrap>
                    <StaffMember username="Ael" avatar="https://a.ppy.sh/7647318?1549056043.png"/>
                    <StaffMember username="akwari" avatar="https://a.ppy.sh/7927754?1516362018.png"/>
                  </v-layout>
                <v-subheader>Shoutcasters <v-icon>record_voice_over</v-icon></v-subheader>
                  <v-layout row wrap>
                    <StaffMember username="Nomme" avatar="https://a.ppy.sh/2359972?1477178502.png"/>
                    <StaffMember username="Shimarin" avatar="https://a.ppy.sh/5442702?1546980840.jpeg"/>
                    <StaffMember username="Zonthem" avatar="https://a.ppy.sh/7193908?1532010175.jpeg"/>
                    <StaffMember username="Zyf" avatar="https://a.ppy.sh/7475179?1533837143.png"/>
                  </v-layout>
              </div>
            </transition>
          </v-flex>
        </v-layout>

      <h2 class="text-xs-center display-1 font-weight-bold">Liste d'inscrits</h2>

      <v-layout row wrap>
        <v-flex lg10 offset-lg1 xl8 offset-xl2>
          <v-list two-line>
            <v-layout row justify-space-between align-center>
              <v-subheader>{{ players.length }} inscrits</v-subheader>

              <v-subheader class="clickable" @click="toggleSort = !toggleSort">
                Trier par rank
                <v-icon :class="{ rotate: toggleSort }">
                  keyboard_arrow_up
                </v-icon>
              </v-subheader>
            </v-layout>

            <PlayerTile
              v-for="player in players"
              :key="player.username"
              :player="player"
            />
          </v-list>

          <v-layout row justify-center>
            <img v-if="!players.length" class="no-players" src="@/assets/no_players.svg" alt="No players registered yet">
          </v-layout>
        </v-flex>
      </v-layout>

    </v-card>
  </v-layout>
</template>

<script>
import PlayerTile from '@/components/PlayerTile.vue'
import StaffMember from '@/components/StaffMember.vue'

export default {
  name: 'Listing',
  components: {
    PlayerTile,
    StaffMember
  },
  data () {
    return {
      isExpanded: true,
      toggleSort: true, // true = desc
      players: []
    }
  },
  created () {
    // Close if it was closed before
    const localIsExpanded = JSON.parse(localStorage.getItem('isExpanded'))
    if (!localIsExpanded) {
      this.isExpanded = false
    }

    this.hydratePlayers()
  },
  methods: {
    toggleStaff () {
      this.isExpanded = !this.isExpanded
      this.handleToggleStaff()
    },
    handleToggleStaff () {
      if (this.isExpanded) {
        localStorage.setItem('isExpanded', true)
      } else {
        localStorage.setItem('isExpanded', false)
      }
    },
    handleSort () {
      if (this.toggleSort) {
        // Asc
        this.players.sort((a, b) => a.rank - b.rank)
      } else {
        // Desc by default
        this.players.sort((a, b) => b.rank - a.rank)
      }
    },
    async hydratePlayers () {
      const data = await (await fetch('/players')).json()
      data.sort((a, b) => a.rank - b.rank)
      this.players = data
    }
  },
  watch: {
    toggleSort () { this.handleSort() }
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
