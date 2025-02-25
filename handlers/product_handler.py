from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from services.device_detection import DeviceDetector
from services.crypto_service import CryptoService
from utils.currency_converter import CurrencyConverter
from database.models import Product, CryptoType
from utils.logger import setup_logger

logger = setup_logger(__name__)

class ProductHandler:
    @staticmethod
    async def display_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_language, user_currency = DeviceDetector.get_user_locale(update)
            db = context.bot_data.get('db')
            
            if not context.args or not context.args[0].isdigit():
                await update.message.reply_text("❌ *Invalid product ID*", parse_mode='MarkdownV2')
                return
                
            product = db.query(Product).get(context.args[0])
            if not product:
                await update.message.reply_text("❌ *Product not found*", parse_mode='MarkdownV2')
                return

            crypto_rates = await CryptoService.get_crypto_rates()
            crypto_savings = CryptoService.calculate_crypto_savings(product.price)
            user_price = await CurrencyConverter.convert(
                product.price,
                product.currency,
                user_currency
            )

            btc_price = crypto_savings[CryptoType.BTC]
            eth_price = crypto_savings[CryptoType.ETH]
            usdt_price = crypto_savings[CryptoType.USDT]

            message = f"""
🎮 *{product.name}*

💰 *Price Options:*
• ₿ BTC: `{btc_price:.8f}` \\(\\-25% OFF\\)
• Ξ ETH: `{eth_price:.6f}` \\(\\-20% OFF\\)
• ₮ USDT: `{usdt_price:.2f}` \\(\\-15% OFF\\)
• 💳 Fiat: `{user_currency} {user_price:.2f}` \\(regular price\\)

⭐️ *Extra Crypto Benefits:*
• Instant delivery
• Extra loyalty points
• Exclusive crypto\\-only deals

📝 *Description:*
_{product.description}_

🔥 *Limited Time Crypto Offer\\!*
"""

            keyboard = [
                [
                    InlineKeyboardButton(f"₿ Pay with BTC", callback_data=f"pay_btc_{product.id}"),
                    InlineKeyboardButton(f"Ξ Pay with ETH", callback_data=f"pay_eth_{product.id}")
                ],
                [InlineKeyboardButton(f"₮ Pay with USDT", callback_data=f"pay_usdt_{product.id}")],
                [InlineKeyboardButton(f"💳 Pay with {user_currency}", callback_data=f"pay_fiat_{product.id}")],
                [InlineKeyboardButton("🔙 Back", callback_data="back_to_products")]
            ]
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                text=message,
                reply_markup=reply_markup,
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Product display error: {str(e)}")
            await update.message.reply_text(
                "❌ *Error displaying product\\. Please try again\\.*",
                parse_mode='MarkdownV2'
            )

    @staticmethod
    async def purchase_with_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            product_id = int(context.args[0])
            db = context.bot_data.get('db')
            
            user = db.query(User).filter_by(telegram_id=update.effective_user.id).first()
            wallet = user.wallet
            product = db.query(Product).get(product_id)
            
            if wallet.balance < product.price:
                await update.message.reply_text(
                    "❌ *Insufficient balance*\n"
                    "Please deposit more funds\\.",
                    parse_mode='MarkdownV2'
                )
                return

            # Process purchase
            wallet.balance -= product.price
            wallet.bonus_points += int(product.price)  # 1 point per dollar
            
            # Create transaction record
            transaction = WalletTransaction(
                wallet_id=wallet.id,
                amount=-product.price,
                type='purchase'
            )
            
            db.add(transaction)
            db.commit()

            await update.message.reply_text(
                f"✅ *Purchase Successful\\!*\n"
                f"Remaining balance: `${wallet.balance:.2f}`\n"
                f"Earned points: `{int(product.price)}`",
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Wallet purchase error: {str(e)}")