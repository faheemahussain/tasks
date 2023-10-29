import requests

# Replace 'YOUR_API_KEY' with your actual Open Exchange Rates API key
API_KEY = 'YOUR_API_KEY'

# Function to fetch the latest exchange rates from the API
def get_exchange_rates(base_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}.json/{API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('rates', {})
    else:
        print("Failed to fetch exchange rates. Check your API key and try again.")
        return None

# Function to perform currency conversion
def convert_currency(amount, from_currency, to_currency, exchange_rates):
    if from_currency == to_currency:
        return amount

    if from_currency in exchange_rates and to_currency in exchange_rates:
        return amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
    else:
        return None

# Main program
if __name__ == '__main__':
    base_currency = input("Enter the base currency code (e.g., USD, EUR): ").upper()
    exchange_rates = get_exchange_rates(base_currency)

    if exchange_rates is not None:
        while True:
            amount = float(input(f"Enter the amount in {base_currency}: "))
            to_currency = input("Enter the target currency code (e.g., EUR, GBP): ").upper()

            converted_amount = convert_currency(amount, base_currency, to_currency, exchange_rates)

            if converted_amount is not None:
                print(f"{amount} {base_currency} is equal to {converted_amount} {to_currency}")
            else:
                print("Invalid currency code. Check your input and try again.")

            another_conversion = input("Perform another conversion? (y/n): ").lower()
            if another_conversion != 'y':
                break

