module.exports = {
  networks: {
      development: {
          host: "localhost",
          port: 7545,
          network_id: "*" // Match any network id
      },
      ganache: {
        host: "206.189.4.230",
        port: 8545,
        network_id: "*" // Match any network id
    }
  }
};