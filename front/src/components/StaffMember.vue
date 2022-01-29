<template>
  <v-flex xs6 sm4 md3 pa-2>

    <a :href="profileUrl" target="_blank" >
      <v-hover>
        <v-layout justify-center align-center column wrap pa-2 v-ripple
          :class="`elevation-${hover ? 4 : 1}`" slot-scope="{ hover }">
            <v-avatar size="48" color="grey lighten-3">
              <img :src="avatar ? avatar : 'https://a.ppy.sh/shrug.png'" :alt="`${username} avatar`">
            </v-avatar>
            <p class="font-weight-bold">{{ username }}</p>
        </v-layout>
      </v-hover>
    </a>

  </v-flex>
</template>

<script>
export default {
  name: 'StaffMember',
  props: {
    username: {
      type: String,
      required: true
    },
    avatar: {
      type: String
    }
  },
  computed: {
    profileUrl () {
      return `https://osu.ppy.sh/users/${this.username}`
    }
  }
}
</script>

<style scoped>

  .layout {
    transition: box-shadow 0.1s;
  }

  a {
    color: black;
    text-decoration: none;
  }

  p {
    margin: 6px 0 0 0;
  }

</style>
