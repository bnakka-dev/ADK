import requests

def get_exchange_rate(base_currency: str, target_currency: str) -> dict:
    """
    Fetches the current exchange rate between two currencies.
    
    Args:
        base_currency: The currency to convert from (e.g., 'USD').
        target_currency: The currency to convert to (e.g., 'INR').
        
    Returns:
        A dictionary containing the exchange rate or an error message.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        rate = response.json()['rates'].get(target_currency)
        return {"status": "success", "rate": rate}
    return {"status": "error", "message": "Could not fetch rate"}