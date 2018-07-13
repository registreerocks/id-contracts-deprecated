# id_contracts

### Setup

1. Clone the repository and navigate inside it

2. Start all docker containers

        $ docker-compose up
    Wait for about a minute until all is configured correctly.

You can explore the API by visiting http://localhost:8085/v0.1/ui/. Note that it will not work because it sends request to port `8080` by default. You will have to copy the curl request to your terminal and change the port to `8085`.

To rebuild the image, call

    $ docker-compose build