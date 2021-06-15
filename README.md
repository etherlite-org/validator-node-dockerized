# How to launch Etherlite validator node with Docker Compose and OpenEthereum

1. Install Docker Engine and Docker Compose following the original instructions https://docs.docker.com/get-docker/ and https://docs.docker.com/compose/install/

2. Clone this repo:

   ```bash
    git clone https://github.com/etherlite-org/validator-node-dockerized
    cd validator-node-dockerized
   ```

3. To be a validator, you need to have a mining address and a private key for it. Name your JSON keystore file as `keystore.json` and put it to the `validator-node-dockerized` directory. Put keystore's password to `password` file.

4. Import your account

   ```bash
   openethereum account import keystore.json --keys-path=data/keys --password=password --chain=etherlite
   ```

5. Copy `.env.example` to `.env` and configure the `.env` file. There are a few settings you need to define:

   ```
   PASSWORD_PATH=/root/password
   EXT_IP=YOUR-EXTERNAL-IP-ADDRESS
   ACCOUNT=0x...
   ```

   - `EXT_IP` - External IP of the current server.
   - `ACCOUNT` - Your mining address (with leading `0x`).

6. Start your node.

   ```bash
   docker-compose up -d
   ```

After docker containers are created, the node will sync with the chain (may take a while).

To restart you need to use `docker-compose stop` and `docker-compose start` being in the `validator-node-dockerized` directory.

