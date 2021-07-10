# How to launch Etherlite validator node with Docker Compose and OpenEthereum

1. Install Docker Engine and Docker Compose following the original instructions https://docs.docker.com/get-docker/ and https://docs.docker.com/compose/install/

2. Clone this repo:

   ```bash
    git clone https://github.com/etherlite-org/validator-node-dockerized
    cd validator-node-dockerized
   ```

3. To be a validator, you need to download the binary from official etherlite 
   ```bash
   apt install -y unzip
   curl -L "https://github.com/etherlite-org/openethereum/releases/download/v3.2.2-rc.1/openethereum-ubuntu20.04.zip" -o openethereum.zip
   unzip openethereum.zip
   ```
4. Create password file for mining account.
   ```bash
   nano password
   ```
   
5. Create your mining account

   ```bash
   openethereum account new --keys-path=data/keys --password=password --chain=etherlite
   ```

6. Copy `.env.example` to `.env` and configure the `.env` file. There are a few settings you need to define:

   ```
   PASSWORD_PATH=/root/password
   EXT_IP=YOUR-EXTERNAL-IP-ADDRESS
   ACCOUNT=0x...
   ```

   - `EXT_IP` - External IP of the current server.
   - `ACCOUNT` - Your mining address (with leading `0x`).

7. Start your node.

   ```bash
   docker-compose up -d
   ```

After docker containers are created, the node will sync with the chain (may take a while).

To restart you need to use `docker-compose stop` and `docker-compose start` being in the `validator-node-dockerized` directory.

