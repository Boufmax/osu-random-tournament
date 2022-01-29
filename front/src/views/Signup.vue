<template>
  <v-layout wrap justify-center fill-height class="mx-3">
    <v-card class="pa-4">
      <v-layout wrap justify-center>
        <img src="@/assets/logo.png" alt="osu!Random Tournament Logo">
      </v-layout>
      <v-layout justify-center class="mt-4">
        <h1>S'inscrire</h1>
      </v-layout>
      <v-card-text class="my-4">
        <transition name="slide-x-transition" mode="out-in">

          <v-form v-if="!isSuccess" ref="form" v-model="valid">
            <v-layout wrap justify-center>
              <v-flex xs12 sm9 md6>
                <v-layout row>
                  <img src="@/assets/osu.svg" alt="osu! logo" class="hidden-xs-only" />
                  <v-text-field
                    v-model="username"
                    label="Pseudo osu!"
                    :rules="usernameRules"
                    validate-on-blur
                    :counter="15"
                    outline
                    required>
                  </v-text-field>
                </v-layout>

                <v-layout row>
                  <img src="@/assets/discord.svg" alt="Discord logo" class="hidden-xs-only" />
                  <v-text-field
                    v-model="discord"
                    label="Pseudo Discord"
                    :rules="discordRules"
                    validate-on-blur
                    outline
                    required>
                  </v-text-field>
                </v-layout>
              </v-flex>
            </v-layout>

            <v-layout justify-center>
              <v-btn color="primary" @click="register" :loading="isLoading">
                S'inscrire
              </v-btn>
            </v-layout>

            <p class="text-xs-center red--text subheading" v-if="error">
              {{ error }}
            </p>
          </v-form>

          <v-layout align-center justify-center column v-if="isSuccess">
            <p class="subheading text-xs-center">
              Votre candidature a été reçu !
              <br>GL & HF
            </p>

            <v-btn color="primary" @click="isSuccess = !isSuccess">Enregistrer une nouvelle personne</v-btn>
          </v-layout>

        </transition>

        <v-layout align-center column wrap mt-5 v-if="alreadySignedUp.length > 0">
          <h2>Vous avez enregistré :</h2>

          <v-flex xs12 sm6 md4>
            <v-chip
              v-for="data in alreadySignedUp"
              :key="data.username"
              color="green"
              text-color="white">
              {{ data.username }} ({{ data.discord }})
            </v-chip>
          </v-flex>
        </v-layout>
      </v-card-text>
    </v-card>
  </v-layout>
</template>

<script>
export default {
  name: 'Signup',
  data () {
    return {
      valid: false,
      username: '',
      discord: '',
      usernameRules: [
        v => !!v || 'Votre pseudo est requis',
        v => v.length < 16 || 'Votre pseudo doit être inférieur à 16 caractères',
        v => v.length >= 3 || 'Votre pseudo doit être supérieur à 2 caractères',
        v => this.validateUsername(v) || 'Vous avez déjà enregistré ce joueur'
      ],
      discordRules: [
        v => !!v || 'Votre pseudo Discord est requis',
        v => v.length >= 2 || 'Votre pseudo doit être supérieur ou égal à 2 caractères',
        v => /^(\S+)#(\d{4})$/.test(v) || 'Pseudo Discord incorrect',
        v => this.validateDiscordUsername(v) || 'Vous avez déjà enregistré ce joueur'
      ],
      isLoading: false,
      isSuccess: false,
      error: null,
      alreadySignedUp: []
    }
  },
  created () {
    this.populateAlreadySignedUp()
  },
  methods: {
    async register () {
      if (this.$refs.form.validate()) {
        this.isLoading = true

        const data = {
          username: this.username,
          discord: this.discord
        }

        try {
          const response = await fetch('/register', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            mode: 'no-cors',
            body: JSON.stringify(data)
          })

          this.isLoading = false

          if (!response.ok) {
            this.error = `${response.status}: ${response.statusText}`
            return
          }

          const localData = JSON.parse(localStorage.getItem('alreadySignedUp'))
          // If already data, push new data
          if (localData) {
            localData.push(data)
            localStorage.setItem('alreadySignedUp', JSON.stringify(localData))
          } else {
            localStorage.setItem('alreadySignedUp', JSON.stringify([data]))
          }

          // Clean up
          this.username = ''
          this.discord = ''
          this.populateAlreadySignedUp()
          this.isSuccess = true
        } catch (error) {
          this.isLoading = false
          console.error(error)
        }
      }
    },
    validateUsername (v) {
      const localData = JSON.parse(localStorage.getItem('alreadySignedUp'))
      if (!localData) return true
      if (localData.find((el) => el.username === v)) return false
      return true
    },
    validateDiscordUsername (v) {
      const localData = JSON.parse(localStorage.getItem('alreadySignedUp'))
      if (!localData) return true
      if (localData.find((el) => el.discord === v)) return false
      return true
    },
    populateAlreadySignedUp () {
      const localData = JSON.parse(localStorage.getItem('alreadySignedUp'))
      if (localData) this.alreadySignedUp = localData
    }
  }
}
</script>

<style scoped>

  .layout:not(:last-child) {
    margin-bottom: 10px;
  }

  form img {
    height: 48px;
    margin: 5px 20px 0 0;
  }

</style>
