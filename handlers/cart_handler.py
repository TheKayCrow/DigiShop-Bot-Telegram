from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.models import Cart, CartItem

class CartHandler:
    @staticmethod
    async def view_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            db = context.bot_data.get('db')
            
            cart = db.query(Cart).filter_by(user_id=user_id).first()
            if not cart or not cart.items:
                await update.message.reply_text(
                    "*🛒 Your cart is empty*",
                    parse_mode='MarkdownV2'
                )
                return

            total = sum(item.product.price * item.quantity for item in cart.items)
            
            message = "*🛒 Your Cart:*\n\n"
            for item in cart.items:
                message += f"• {item.product.name} x{item.quantity}\n"
            message += f"\n*Total: ${total:.2f}*"

            keyboard = [
                [InlineKeyboardButton("💳 Checkout", callback_data="checkout")],
                [InlineKeyboardButton("🗑️ Clear Cart", callback_data="clear_cart")]
            ]
            
            await update.message.reply_text(
                message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Cart error: {str(e)}")