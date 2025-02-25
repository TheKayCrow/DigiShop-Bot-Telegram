import asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config.config import Config
from src.handlers import Handlers, CategoryHandler
from utils.logger import setup_logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
from database.init_categories import init_categories
from handlers.section_handler import SectionHandler
from handlers.wallet_handler import WalletHandler
from handlers import CryptoHandler

logger = setup_logger()

def setup_database():
    engine = create_engine(Config.DATABASE_URL)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

async def main():
    try:
        # Setup database
        Session = setup_database()
        db = Session()
        init_categories(db)

        # Initialize bot
        app = (
            Application.builder()
            .token(Config.BOT_TOKEN)
            .build()
        )
        app.bot_data['db'] = db

        # Add handlers
        app.add_handler(CommandHandler("start", CryptoHandler.start))
        app.add_handler(CommandHandler("categories", CategoryHandler.show_categories))
        app.add_handler(CommandHandler("sections", SectionHandler.show_sections))
        app.add_handler(CommandHandler("wallet", WalletHandler.show_wallet))
        app.add_handler(CommandHandler("deposit", WalletHandler.process_deposit))
        app.add_handler(CallbackQueryHandler(
            CategoryHandler.show_subcategories,
            pattern="^cat_"
        ))
        app.add_handler(CallbackQueryHandler(
            SectionHandler.show_top_products,
            pattern="^section_top"
        ))
        app.add_handler(CallbackQueryHandler(
            WalletHandler.process_deposit,
            pattern="^dep_"
        ))

        # Start polling
        logger.info("Bot started successfully!")
        await app.run_polling()

    except Exception as e:
        logger.error(f"Error starting bot: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    asyncio.run(main())