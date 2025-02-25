from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.models import Product
from sqlalchemy import or_

class SearchHandler:
    @staticmethod
    async def search_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            query = " ".join(context.args)
            db = context.bot_data.get('db')
            
            products = db.query(Product).filter(
                or_(
                    Product.name.ilike(f"%{query}%"),
                    Product.description.ilike(f"%{query}%")
                )
            ).limit(10).all()

            keyboard = [
                [InlineKeyboardButton(
                    f"🏷️ {p.name} - {p.price:.2f}$",
                    callback_data=f"product_{p.id}"
                )] for p in products
            ]
            keyboard.append([InlineKeyboardButton("🔙 Back", callback_data="back_to_menu")])
            
            await update.message.reply_text(
                "*🔍 Search Results:*",
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Search error: {str(e)}")