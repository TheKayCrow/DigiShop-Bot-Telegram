from typing import Dict
from database.models import Language

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "welcome": {
        "en": "Welcome to DigiShop! 🛍️\nSelect your preferred language:",
        "it": "Benvenuto su DigiShop! 🛍️\nSeleziona la tua lingua preferita:",
        "es": "¡Bienvenido a DigiShop! 🛍️\nSelecciona tu idioma preferido:",
        "fr": "Bienvenue sur DigiShop! 🛍️\nSélectionnez votre langue :",
        "de": "Willkommen bei DigiShop! 🛍️\nWählen Sie Ihre Sprache:"
    },
    "top_products": {
        "en": "🏆 Top Products",
        "it": "🏆 Prodotti Top",
        "es": "🏆 Productos Destacados",
        "fr": "🏆 Produits Phares",
        "de": "🏆 Top-Produkte"
    }
    # Add more translations as needed
}

class Localizer:
    @staticmethod
    def get_text(key: str, lang: Language = Language.EN) -> str:
        return TRANSLATIONS.get(key, {}).get(lang.value, TRANSLATIONS[key]["en"])