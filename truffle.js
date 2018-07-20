module.exports = {
  networks: {
      development: {
          host: "localhost",
          port: 7545,
          network_id: "*" // Match any network id
      },
      ganache: {
        host: "159.65.197.244",
        port: 8545,
        network_id: "*" // Match any network id
    }
  }
};
