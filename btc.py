import sys
import requests
key = "https://api.coindesk.com/v1/bpi/currentprice.json"
dade = requests.get(key)
#
dade = dade.json()
btc = dade["bpi"]["USD"]["rate_float"]
try:
    if len(sys.argv) != 2 :
        sys.exit("Missing command-line argument")
    elif len(sys.argv) == 2 :
        if float(sys.argv[1]):
            num = float(sys.argv[1])
            print(f"${btc*num:,.4f}")
except ValueError :
    sys.exit("Command-line argument is not a number")
