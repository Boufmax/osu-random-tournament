<template>
  <nav>
    <v-toolbar class="indigo lighten-1" height="80" dark>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>

      <v-layout row wrap justify-center>
        <v-toolbar-title class="px-2">
          <v-layout align-center>
            <img class="navbar-logo" src="@/assets/logo.png" alt="osu!Random logo">
            <router-link to="/" class="ml-2">
              osu!Random tournament
            </router-link>
          </v-layout>
        </v-toolbar-title>
      </v-layout>
    </v-toolbar>

    <v-toolbar color="primary" dark dense class="hidden-xs-only">
      <v-layout justify-center fill-height>
        <v-toolbar-items>
          <v-layout row wrap fill-height>
            <v-btn v-for="link in staticRoutes" :key="link.name" :to="link.path" flat>
              {{ link.meta.title }}
            </v-btn>
          </v-layout>
        </v-toolbar-items>
      </v-layout>
    </v-toolbar>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary>

      <div class="pl-5 pt-5">
        <v-icon
          class="close-drawer"
          @click="drawer = !drawer"
          size="30"
        >
          close
        </v-icon>
        <h3 class="headline font-weight-bold">Menu</h3>
      </div>

      <v-list class="pt-4 pl-4">
        <v-list-tile
          v-for="link in staticRoutes"
          :key="link.name"
          :to="link.path"
          ripple
          class="py-1">
          <v-list-tile-action>
            <v-icon>{{ link.meta.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title class="font-weight-bold">{{ link.meta.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <ul class="additional-links mt-5">
          <li v-for="link in subLinks" :key="link.title">
            <a :href="link.href">{{ link.title }}</a>
          </li>
        </ul>
      </v-list>
    </v-navigation-drawer>
  </nav>
</template>

<script>
import { staticRoutes } from '../router'

export default {
  name: 'Navbar',
  data () {
    return {
      drawer: false,
      staticRoutes,
      subLinks: [
        {
          title: 'Topic',
          href: '#'
        },
        {
          title: 'Discord',
          href: 'https://discord.gg/C3A6A27'
        }
      ]
    }
  }
}
</script>

<style scoped>

  .navbar-logo {
    height: 48px;
  }

  .close-drawer {
    margin-bottom: 14px;
  }

  .v-toolbar__title {
    margin: 0;
  }

  .router-link-active {
    color: white;
    text-decoration: none;
  }

  .additional-links {
    list-style-type: none;
  }
  .additional-links li {
    margin-bottom: 20px;
  }
  .additional-links li > a {
    color: black;
    text-decoration: none;
  }

</style>
