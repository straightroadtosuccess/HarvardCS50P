import requests
import sys

# rest.coincap.io/v3/assets/bitcoin?apiKey=24b325beae07203725aee4e78057eebd0cb6f580f3fa7e4330a8f91e5f30fdbe

try:
    # Check if amount of CLA's are correct
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    else:
        # Assign a variable and convert to float
        x = float(sys.argv[1])
        # Handle requests and json data
        r = requests.get(
            'http://rest.coincap.io/v3/assets/bitcoin?apiKey=24b325beae07203725aee4e78057eebd0cb6f580f3fa7e4330a8f91e5f30fdbe')
        data = r.json()
        # print(data)
        # Convert json table priceUsd to math operation ready readable number
        amount = float(data['data']['priceUsd'])
        # Multiply the price by the quantity desired to be purchased
        cost = amount * x
        # Print the result!
        print(f"${cost:,.4f}")

# Check if CLA is an int
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

# Handle server side requests or other request error
except requests.RequestException:
    sys.exit(1)
