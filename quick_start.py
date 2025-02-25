from telegram.ext import Application, CommandHandler
from config import Config

INITIAL_PRODUCTS = {
    "netflix": {
        "name": "Netflix Premium",
        "prices": {
            "btc": 0.0012,  # Circa $50 con sconto crypto
            "eth": 0.028,
            "usdt": 48.00
        },
        "description": "Netflix Premium Account | 4K UHD | 4 Screens"
    },
    "spotify": {
        "name": "Spotify Premium",
        "prices": {
            "btc": 0.00024,  # Circa $10 con sconto crypto
            "eth": 0.0056,
            "usdt": 9.50
        },
        "description": "Spotify Premium Account | Individual Plan"
    }
}