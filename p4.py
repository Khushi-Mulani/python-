import requests

def get_exchange_rates(api_key, base_currency='USD'):
    """Fetches real-time exchange rates from ExchangeRate-API."""
    url = f"https://exchangerate-api.com{api_key}/latest/{base_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status() # Raise exception for HTTP errors
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates']
        else:
            print("Error fetching data:", data.get('error-type'))
            return None
    except requests.exceptions.RequestException as e:
        print("API Request failed:", e)
        return None

def convert_currency(amount, from_curr, to_curr, rates):
    """Converts amount from one currency to another using provided rates."""
    if from_curr == to_curr:
        return amount
    
    # Conversion logic: (Amount / FromRate) * ToRate
    # This works because all rates are relative to a base currency
    if from_curr in rates and to_curr in rates:
        # Convert to base currency, then to target currency
        converted = (amount / rates[from_curr]) * rates[to_curr]
        return round(converted, 2)
    else:
        print("One or both currency codes are invalid.")
        return None

def main():
    # 1. Sign up at https://www.exchangerate-api.com/ to get a free API key
    API_KEY = "YOUR_API_KEY_HERE" 
    
    print("--- Currency Converter ---")
    
    # Get user input
    try:
        from_curr = input("Enter source currency (e.g., USD, EUR): ").upper()
        to_curr = input("Enter target currency (e.g., INR, GBP): ").upper()
        amount = float(input(f"Enter amount in {from_curr}: "))
    except ValueError:
        print("Invalid amount entered.")
        return

    # Fetch rates
    rates = get_exchange_rates(API_KEY, from_curr)
    
    if rates:
        result = convert_currency(amount, from_curr, to_curr, rates)
        if result is not None:
            print(f"\n{amount} {from_curr} = {result} {to_curr}")
            print(f"Rate: 1 {from_curr} = {round(rates[to_curr]/rates[from_curr], 4)} {to_curr}")

if __name__ == "__main__":
    main()
