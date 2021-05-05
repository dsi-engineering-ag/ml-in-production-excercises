module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    proxy: "http://localhost:8000/",
    port: 8081
  },
};
