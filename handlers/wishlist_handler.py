from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.models import Wishlist

class WishlistHandler:
    @staticmethod
    async def view_wishlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            db = context.bot_data.get('db')
            
            wishlist = db.query(Wishlist).filter_by(user_id=user_id).first()
            if not wishlist or not wishlist.products:
                await update.message.reply_text(
                    "*💝 Your wishlist is empty*",
                    parse_mode='MarkdownV2'
                )
                return

            message = "*💝 Your Wishlist:*\n\n"
            keyboard = []
            
            for product in wishlist.products:
                message += f"• {product.name} \- ${product.price:.2f}\n"
                keyboard.append([
                    InlineKeyboardButton(
                        f"🛒 Add {product.name}",
                        callback_data=f"add_to_cart_{product.id}"
                    )
                ])
            
            keyboard.append([
                InlineKeyboardButton("🔙 Back", callback_data="back_to_menu")
            ])
            
            await update.message.reply_text(
                message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Wishlist error: {str(e)}")