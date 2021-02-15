<template>
  <div class="container">
    <img src="@/assets/logo.png" alt="logo" />

    <p>
      PsyBot est un projet qui consiste à créer un Chatbot basant sur un système
      questions / réponses. L’objectif du projet est d’apporter du soleil à tous
      ceux qui souffrent mentalement à cause du confinement et des situations sanitaires
      actuelles. À la fondation du projet, son orientation principale était
      d’aider les patients ou les patients potentiels atteints de maladies
      psychologiques à sortir de leurs difficultés. Au fur et à mesure que la
      base de données s’enrichissait, le projet a abordé d’autres aspects du
      domaine médical, tels que les comparaisons des cas, le dosage et la durée
      d’un certain médicament, ou des connaissances médicales de base.
    </p>

    <p>
      Avec l’aide de leur aimable professeur M. Gaël Lejeune, deux étudiantes à
      la Sorbonne Université – Nishan TANG et Can CUI, ont travaillé assidûment
      pour la naissance de leur bébé Bot Palette, enfant nourrie de douceur et
      d’amour.
    </p>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 10px 60px 30px;
  box-sizing: border-box;
}

img {
  margin: 0 auto;
  width: 60%;
}

p {
  font-size: 18px;
  word-wrap: break-word;
  word-break: normal;
  line-height: 1.5;
}

p ~ p {
  margin-top: 12px;
}
</style>
