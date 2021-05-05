<template>
  <v-container style="padding-left: 100px; padding-right: 100px">
    <a id="order">
    <v-row>
      <v-col>
        <h2 class="section-title mt-0" align="center">Order Your Car</h2>
      </v-col>
    </v-row>
    </a>
    <v-row>
      <v-col align="center" v-for="car in cars" :key="car.name" cols="4">
        <v-card
          @click="selectCar(car)"
          :class="{ 'car-selected': car == selectedCar }"
        >
          <v-img height="200" :src="car.image"></v-img>

          <v-card-title>{{ car.name }}</v-card-title>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <label>Information for your order</label>
        <v-slider
          label="Yearly income"
          hint="Yearly Income"
          max="100000"
          min="0"
          v-model="selectedIncome"
        >
          <template v-slot:append>
            {{ formatPrice(selectedIncome) }}
          </template>
        </v-slider>
      </v-col>
    </v-row>
    <v-row>
      <v-col align="center">
        <v-btn
          elevation="2"
          :color="ordered ? 'green' : 'primary'"
          :loading="ordering"
          :disabled="!selectedCar"
          @click="order()"
        >
          {{ ordered ? "Ordered" : "Order now" }}
        </v-btn>
      </v-col>
    </v-row>

    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title> Order not possible at the moment </v-card-title>

        <v-card-text>
          We are sorry. We only have a limited supply.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" text @click="complain()"> Complain! </v-btn>
          <v-btn color="primary" text @click="badLuck()"> Bad luck! </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<style lang="scss">
.car-selected {
  outline: solid 3px cornflowerblue !important;
}
</style>

<script>
import Axios from "axios";

export default {
  name: "Home",
  data: () => ({
    dialog: false,
    ordering: false,
    ordered: false,

    cars: [
      { name: "ID.3", price: 50000, image: "images/id3.jpg" },
      { name: "Enyaq", price: 100000, image: "images/enyaq.jpg" },
      { name: "Model S", price: 200000, image: "images/models.jpg" },
    ],

    selectedCar: null,
    selectedIncome: null,
  }),
  methods: {
    order() {
      this.ordering = true;

      Axios.post("/api/v1/predict", {
        data: { ndarray: [[this.selectedCar.price, this.selectedIncome]] },
      })
        .then((response) => {
          if (response.data.data.ndarray[0] == 0) {
            this.dialog = true;
          } else {
            this.ordered = true;
          }
        })
        .finally((this.ordering = false));
    },
    badLuck() {
      this.dialog = false;
      this.ordering = false;
    },
    complain() {
      this.dialog = false;
      this.ordering = false;
    },
    formatPrice(value) {
      let val = (value / 1).toFixed(2);
      return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "'");
    },
    selectCar(car) {
      this.selectedCar = car;
    },
  },
};
</script>
