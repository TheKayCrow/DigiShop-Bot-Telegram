from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.models import Wallet, WalletTransaction
from utils.bonus_calculator import calculate_bonus

class WalletHandler:
    MINIMUM_DEPOSIT = 10.0  # Minimum deposit amount
    
    @staticmethod
    async def show_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            db = context.bot_data.get('db')
            wallet = db.query(Wallet).filter_by(user_id=user_id).first()
            
            message = f"""
💰 *Your Wallet*

Current Balance: `${wallet.balance:.2f}`
Bonus Points: `{wallet.bonus_points} pts`
Deposit Tier: {get_tier_emoji(wallet.balance)}

*Deposit Bonuses:*
• $50\\+ \\= 5% bonus
• $100\\+ \\= 10% bonus
• $200\\+ \\= 15% bonus
• $500\\+ \\= 20% bonus

*Minimum Deposit:* `${WalletHandler.MINIMUM_DEPOSIT:.2f}`
"""
            keyboard = [
                [InlineKeyboardButton("💵 Deposit", callback_data="deposit")],
                [InlineKeyboardButton("📊 Transaction History", callback_data="history")],
                [InlineKeyboardButton("🛍️ Shop with Balance", callback_data="shop")]
            ]
            
            await update.message.reply_text(
                text=message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Wallet display error: {str(e)}")

    @staticmethod
    async def process_deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            amount = float(context.args[0])
            if amount < WalletHandler.MINIMUM_DEPOSIT:
                await update.message.reply_text(
                    f"❌ Minimum deposit is ${WalletHandler.MINIMUM_DEPOSIT:.2f}"
                )
                return

            bonus = calculate_bonus(amount)
            total = amount + bonus

            message = f"""
💎 *Deposit Summary*

Amount: `${amount:.2f}`
Bonus: `${bonus:.2f}` \\(\\+{(bonus/amount)*100:.0f}%\\)
*Total Credit:* `${total:.2f}`

Select payment method:
"""
            keyboard = [
                [
                    InlineKeyboardButton("💳 Card", callback_data=f"dep_card_{amount}"),
                    InlineKeyboardButton("₿ Crypto", callback_data=f"dep_crypto_{amount}")
                ],
                [InlineKeyboardButton("🔙 Back", callback_data="back_to_wallet")]
            ]

            await update.message.reply_text(
                text=message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )

        except Exception as e:
            logger.error(f"Deposit error: {str(e)}")