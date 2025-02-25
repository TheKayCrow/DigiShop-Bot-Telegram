from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config.casino_config import CASINO_AFFILIATES
from utils.logger import setup_logger

logger = setup_logger(__name__)

class CasinoHandler:
    @staticmethod
    async def show_casinos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            message = """
🎰 *Premium Casino Partners*

💎 *Benefits:*
• Instant Registration
• Crypto Deposits/Withdrawals
• Exclusive Bonuses
• 24/7 Support

🎁 *Special Offer:*
Get extra bonus using our links\\!
"""
            keyboard = []
            for casino_id, casino in CASINO_AFFILIATES.items():
                keyboard.append([
                    InlineKeyboardButton(
                        f"🎲 {casino['name']} | {casino['bonus']}",
                        callback_data=f"casino_{casino_id}"
                    )
                ])
            
            keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="back_to_menu")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                text=message,
                reply_markup=reply_markup,
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Casino display error: {str(e)}")