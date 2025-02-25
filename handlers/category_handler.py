from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes
from database.models import Category
from utils.logger import setup_logger

logger = setup_logger()

class CategoryHandler:
    @staticmethod
    async def show_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            main_categories = context.bot_data.get('db').query(Category).filter_by(parent_id=None).all()
            
            keyboard = []
            for cat in main_categories:
                keyboard.append([
                    InlineKeyboardButton(f"📁 {cat.name}", callback_data=f"cat_{cat.id}")
                ])
            
            keyboard.append([InlineKeyboardButton("🏠 Main Menu", callback_data="main_menu")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                "🗂 Choose a category:",
                reply_markup=reply_markup
            )
            
        except Exception as e:
            logger.error(f"Error showing categories: {str(e)}")
            await update.message.reply_text("Error loading categories. Please try again.")

    @staticmethod
    async def show_subcategories(update: Update, context: ContextTypes.DEFAULT_TYPE, category_id: int):
        try:
            db = context.bot_data.get('db')
            
            # Get main category name
            main_category = db.query(Category).filter_by(id=category_id).first()
            subcategories = db.query(Category).filter_by(parent_id=category_id).all()
            
            keyboard = []
            for subcat in subcategories:
                keyboard.append([
                    InlineKeyboardButton(f"📑 {subcat.name}", callback_data=f"subcat_{subcat.id}")
                ])
            
            keyboard.append([InlineKeyboardButton("⬅️ Back", callback_data="categories")])
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.callback_query.edit_message_text(
                f"📁 {main_category.name} - Select a subcategory:",
                reply_markup=reply_markup
            )
            
        except Exception as e:
            logger.error(f"Error showing subcategories: {str(e)}")
            await update.callback_query.answer("Error loading subcategories. Please try again.")