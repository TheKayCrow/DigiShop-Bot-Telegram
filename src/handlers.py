from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from sqlalchemy.orm import Session
from . import models
from utils.logger import setup_logger
from database.connection import get_db
from database.models import User, Product

logger = setup_logger(__name__)

class Handlers:
    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            username = update.effective_user.username
            
            db = next(get_db())
            user = db.query(User).filter_by(telegram_id=user_id).first()
            
            if not user:
                new_user = User(telegram_id=user_id, username=username)
                db.add(new_user)
                db.commit()
            
            await update.message.reply_text(
                f"Welcome to DigiShop! 🛍️\n"
                f"Use /help to see available commands."
            )
        except Exception as e:
            logger.error(f"Error in start handler: {str(e)}")
            await update.message.reply_text("An error occurred. Please try again later.")