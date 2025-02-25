from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

class TrustHandler:
    @staticmethod
    async def show_verification(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            message = """
✅ *Trust & Safety*

🛡️ *Our Guarantees:*
• Verified Casino Partners
• Protected Transactions
• 24/7 Support Access
• Money\\-back Guarantee
• Community Reviews

📊 *Statistics:*
• Active Users: 5000\\+
• Transactions: 50000\\+
• Rating: 4\\.9/5
• Support Response: <15 min

💫 *Featured Partners:*
• Ninlay Play
• Crown Slots
• Loki Casino
• OnLuck
"""
            await update.message.reply_text(
                text=message,
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Trust display error: {str(e)}")