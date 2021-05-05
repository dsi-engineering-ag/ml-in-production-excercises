<template>
  <v-app >
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<style lang="scss">
.v-application--wrap {
  min-height: 0 !important;
}
</style>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
