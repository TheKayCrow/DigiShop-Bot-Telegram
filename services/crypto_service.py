from typing import Dict
import aiohttp
from database.models import CryptoType

class CryptoService:
    @staticmethod
    async def get_crypto_rates() -> Dict[str, float]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.coingecko.com/api/v3/simple/price",
                params={
                    "ids": "bitcoin,ethereum,tether",
                    "vs_currencies": "usd"
                }
            ) as response:
                data = await response.json()
                return {
                    CryptoType.BTC: data['bitcoin']['usd'],
                    CryptoType.ETH: data['ethereum']['usd'],
                    CryptoType.USDT: data['tether']['usd']
                }

    @staticmethod
    def calculate_crypto_savings(price: float) -> Dict[str, float]:
        """Calculate apparent savings in crypto"""
        return {
            CryptoType.BTC: price * 0.85,  # 15% apparent discount
            CryptoType.ETH: price * 0.88,  # 12% apparent discount
            CryptoType.USDT: price * 0.90  # 10% apparent discount
        }