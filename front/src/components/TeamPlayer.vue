<template>
  <v-flex xs12 md6
    class="team-player"
  >

    <a :href="`https://osu.ppy.sh/users/${player.osu_id}`" target="_blank" rel="nofollow noopener noreferrer">

      <v-card v-ripple>
        <div
          class="v-avatar-container"
          :style="`background-image: url(${coverImage})`"
        >
          <v-chip class="absolute-left">
            <v-avatar>
              <v-icon size="20">grade</v-icon>
            </v-avatar>
            {{ player.qualifier_score }}
          </v-chip>

          <v-chip class="absolute-right">
            #{{ rank }}
          </v-chip>

          <v-avatar class="v-avatar-overlapped absolute-center" size="90">
            <img
              :src="`https://a.ppy.sh/${player.osu_id}`"
              :alt="`${player.username}'s avatar`"
            />

            <strong class="v-avatar-username absolute-center">{{ player.username }}</strong>
          </v-avatar>
        </div>

      </v-card>

    </a>

  </v-flex>
</template>

<script>
import formatRank from '../utils/formatRank'

export default {
  name: 'TeamPlayer',
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
    coverImage () {
      const randomPictureIndex = Math.floor(Math.random() * Math.floor(8)) + 1

      return (
        `https://osu.ppy.sh/images/headers/profile-covers/c${randomPictureIndex}.jpg`
      )
    }
  }
}
</script>

<style scoped>

  .team-player {
    cursor: pointer;
    padding: 0 80px;
    margin-bottom: 36px;
  }

  .v-avatar-container {
    height: 90px;
    position: relative;
    background-blend-mode: lighten;
  }

  .v-avatar-container:hover .v-avatar-username {
    opacity: 0;
  }

  .v-avatar-container:hover .v-avatar-overlapped img {
    filter: brightness(100%);
  }

  .v-avatar-overlapped {
    bottom: -18px;
  }

  .v-avatar-overlapped img {
    filter: brightness(50%);
    transition: filter 0.2s;
  }

  .v-avatar-username {
    bottom: 26px;
    font-size: 22px;
    letter-spacing: 2px;
    color: white;
    text-shadow: 0px 0px 16px black;
    transition: opacity 0.2s;
  }

  .absolute-right {
    position: absolute;
    top: 4px;
    right: 4px;
    font-weight: bold;
  }

  .absolute-left {
    position: absolute;
    top: 4px;
    left: 4px;
    font-weight: bold;
  }

  .absolute-left .v-avatar {
    margin-right: 0;
  }

  .absolute-center {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
  }

  @media screen and (max-width: 600px) {
    .team-player {
      padding: 0;
    }
  }

</style>
