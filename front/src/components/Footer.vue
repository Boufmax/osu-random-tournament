<template>
  <v-footer height="auto" dark>
    <v-layout justify-center row wrap>
      <v-btn
        v-for="link in links"
        :key="link.title"
        :href="link.href"
        target="_blank"
        flat
        round>
        {{ link.title }}
      </v-btn>
      <v-flex black xs12 text-xs-center py-3>
        <v-layout justify-space-between row wrap>
          <v-flex xs12 md4>
            <p>❤️</p>
          </v-flex>
          <v-flex xs12 md4>
            <p>Développé par <a href="https://twitter.com/KeziahMoselle">Nemesis-</a> et <a href="https://twitter.com/BoufDxD">Bouf</a></p>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  name: 'Footer',
  data () {
    return {
      links: [
        {
          title: 'Topic',
          href: '#'
        },
        {
          title: 'Discord',
          href: 'https://discord.gg/C3A6A27'
        },
        {
          title: '@BoufDxD',
          href: 'https://twitter.com/BoufDxD'
        },
        {
          title: '@rolitchi',
          href: 'https://twitter.com/rolitchi'
        }
      ]
    }
  }
}
</script>

<style scoped>

  footer p {
    margin: 0;
  }

  .flex.black a {
    color: #29b;
    text-decoration: none;
  }

  .flex.black a:hover {
    text-decoration: underline;
  }

</style>
