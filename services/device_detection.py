from telegram import Update
import locale
import pycountry

class DeviceDetector:
    @staticmethod
    def get_user_locale(update: Update) -> tuple:
        # Get language from Telegram client
        user_language = update.effective_user.language_code or 'en'
        
        try:
            # Get system locale for currency
            system_locale = locale.getlocale()[0]
            country_code = system_locale.split('_')[1]
            currency = pycountry.currencies.get(numeric=country_code)
            currency_code = currency.alpha_3 if currency else 'USD'
        except:
            currency_code = 'USD'
            
        return user_language, currency_code