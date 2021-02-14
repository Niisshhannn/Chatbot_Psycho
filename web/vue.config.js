module.exports = {
  publicPath: "./",
  assetsDir: "static",
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        changeOrigin: true,
      },
    },
  },
};
