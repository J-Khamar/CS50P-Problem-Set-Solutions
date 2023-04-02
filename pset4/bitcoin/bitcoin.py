import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        factor = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("Unable to query api")
    sys.exit()

bitcoin_info = r.json()

for index, value in bitcoin_info.items():
    if index == "bpi":
        for currency, item in value.items():
            if item["code"] == "USD":
                rate = item["rate"]

rate = factor * float(rate.replace(",", ""))
print(f"${rate:,.4f}")




