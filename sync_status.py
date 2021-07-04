import requests
import json
import time
from babel.numbers import format_currency

url = "http://localhost:8545/"

payload = json.dumps({
    "jsonrpc": "2.0",
    "method": "eth_syncing",
    "params": [],
    "id": 1
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
data = response.json()['result']

starttime = time.time()
while True:
    highestBlock = int(data['highestBlock'], 16)
    currentBlock = int(data['currentBlock'], 16)

    print(format_currency(highestBlock, 'INR', locale='en_IN')[1:])
    print(format_currency(currentBlock, 'INR', locale='en_IN')[1:])
    print(format_currency(highestBlock -
          currentBlock, 'INR', locale='en_IN')[1:])

    print()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
