from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class CryptoHandler:
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message = """
💎 *Welcome to DigiShop Bot*
Your crypto\\-first digital marketplace\\!
        """
        await update.message.reply_text(text=message, parse_mode='MarkdownV2')