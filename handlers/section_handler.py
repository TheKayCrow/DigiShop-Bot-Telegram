from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from services.product_ranking import ProductRanking
from utils.localization import Localizer
from database.models import UserPreferences, Language

class SectionHandler:
    @staticmethod
    async def show_sections(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        db = context.bot_data.get('db')
        
        user_pref = db.query(UserPreferences).filter_by(user_id=user_id).first()
        lang = user_pref.language if user_pref else Language.EN
        
        keyboard = [
            [InlineKeyboardButton(Localizer.get_text("top_products", lang), 
                                callback_data="section_top")],
            [InlineKeyboardButton("🌟 Best Rated", callback_data="section_rated")],
            [InlineKeyboardButton("📈 Best Sellers", callback_data="section_sellers")]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "Choose a section:",
            reply_markup=reply_markup
        )

    @staticmethod
    async def show_top_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
        db = context.bot_data.get('db')
        products = ProductRanking.get_top_products(db)
        
        # Show products in a formatted way
        message = "🏆 Top Products:\n\n"
        for product in products:
            message += f"- {product.name} ({product.currency.value} {product.price})\n"
        
        await update.callback_query.edit_message_text(message)