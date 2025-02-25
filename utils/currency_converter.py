from typing import Dict
import aiohttp
from database.models import Currency

class CurrencyConverter:
    API_KEY = "your_exchange_rate_api_key"
    
    @staticmethod
    async def get_rates() -> Dict[str, float]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.exchangerate-api.com/v4/latest/USD"
            ) as response:
                data = await response.json()
                return data['rates']

    @staticmethod
    async def convert(amount: float, from_currency: Currency, 
                     to_currency: Currency) -> float:
        if from_currency == to_currency:
            return amount
            
        rates = await CurrencyConverter.get_rates()
        usd_amount = amount / rates[from_currency.value]
        return usd_amount * rates[to_currency.value]