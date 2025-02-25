from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.crypto_service import CryptoService
from utils.crypto_bonus import CryptoBonus

class CryptoWalletHandler:
    @staticmethod
    async def show_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            db = context.bot_data.get('db')
            wallet = db.query(CryptoWallet).filter_by(user_id=user_id).first()
            
            # Get current crypto rates
            rates = await CryptoService.get_crypto_rates()
            
            message = f"""
💎 *Your Crypto Wallet*

*Balances:*
• ₿ BTC: `{wallet.btc_balance:.8f}` \\($\\{wallet.btc_balance * rates['BTC']:.2f}\\)
• Ξ ETH: `{wallet.eth_balance:.6f}` \\($\\{wallet.eth_balance * rates['ETH']:.2f}\\)
• ₮ USDT: `{wallet.usdt_balance:.2f}`

🏆 *Loyalty Points:* `{wallet.loyalty_points}`

*Deposit Bonuses:*
• BTC: `+25%` base \\+ `10%` for 0\\.1\\+ BTC
• ETH: `+20%` base \\+ `8%` for 1\\.0\\+ ETH
• USDT: `+15%` base \\+ `5%` for 100\\+ USDT

💡 *Tip:* Crypto deposits get extra bonuses\\!
"""
            keyboard = [
                [
                    InlineKeyboardButton("₿ Deposit BTC", callback_data="dep_btc"),
                    InlineKeyboardButton("Ξ Deposit ETH", callback_data="dep_eth")
                ],
                [InlineKeyboardButton("₮ Deposit USDT", callback_data="dep_usdt")],
                [InlineKeyboardButton("📊 Transaction History", callback_data="crypto_history")]
            ]
            
            await update.message.reply_text(
                text=message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Crypto wallet display error: {str(e)}")