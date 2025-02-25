from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.models import User, ReferralUser
from utils.logger import setup_logger

logger = setup_logger(__name__)

class UserPanelHandler:
    @staticmethod
    async def show_main_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            db = context.bot_data.get('db')
            user = db.query(User).filter_by(telegram_id=user_id).first()
            ref_user = db.query(ReferralUser).filter_by(user_id=user.id).first()

            message = f"""
🎮 *DigiShop Dashboard*

💰 *Your Balance:*
• Wallet: `${user.wallet.balance:.2f}`
• Bonus Points: `{user.wallet.bonus_points}`
• Referral Earnings: `${ref_user.total_earnings if ref_user else 0:.2f}`

🎰 *Casino Partners:*
• Active Partners: `18`
• Special Bonuses: `Available`
• Exclusive Deals: `Daily`

📈 *Earning Options:*
• Casino Affiliation
• Digital Products
• Referral Program
• Loyalty Rewards

🏆 *Your Status:* {get_user_tier_emoji(user)}
"""
            keyboard = [
                [
                    InlineKeyboardButton("🎰 Casinos", callback_data="show_casinos"),
                    InlineKeyboardButton("💰 Deposit", callback_data="deposit")
                ],
                [
                    InlineKeyboardButton("👥 Referral", callback_data="referral"),
                    InlineKeyboardButton("🎁 Rewards", callback_data="rewards")
                ],
                [
                    InlineKeyboardButton("📊 Statistics", callback_data="stats"),
                    InlineKeyboardButton("⚙️ Settings", callback_data="settings")
                ]
            ]

            await update.message.reply_text(
                text=message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )

        except Exception as e:
            logger.error(f"Panel display error: {str(e)}")