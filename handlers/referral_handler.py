from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.models import User, Referral
from utils.logger import setup_logger
from services.anti_abuse import AntiAbuseService

logger = setup_logger()

class ReferralHandler:
    @staticmethod
    async def create_referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            db = context.bot_data.get('db')
            
            ref_user = db.query(ReferralUser).filter_by(user_id=user_id).first()
            if not ref_user:
                ref_code = f"REF{user_id}{datetime.utcnow().strftime('%y%m%d')}"
                ref_user = ReferralUser(
                    user_id=user_id,
                    referral_code=ref_code
                )
                db.add(ref_user)
                db.commit()

            message = f"""
🎯 *Your Referral Dashboard*

📊 *Your Stats:*
• Total Earnings: `${ref_user.total_earnings:.2f}`
• Active Referrals: `{len(ref_user.referrals)}`
• Status: `{'🟢 Active' if not ref_user.is_banned else '🔴 Banned'}`

🎁 *Rewards:*
• Casino Sign\\-up: `25%`
• Deposits: `10%`
• Activity: `5%`

📋 *Your Referral Code:*
`{ref_user.referral_code}`

⚠️ *Anti\\-Abuse Policy:*
• Max {AntiAbuseService.MAX_DAILY_REFERRALS} referrals per day
• Real users only
• No self\\-referrals
• No VPN/Proxy
"""
            await update.message.reply_text(
                text=message,
                parse_mode='MarkdownV2'
            )
            
        except Exception as e:
            logger.error(f"Referral error: {str(e)}")

    @staticmethod
    async def generate_ref_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        ref_code = f"ref_{user_id}"
        bot_username = context.bot.username
        
        ref_link = f"https://t.me/{bot_username}?start={ref_code}"
        
        await update.message.reply_text(
            f"🎯 Here's your referral link:\n{ref_link}\n\n"
            "Share this link with friends and earn commissions on their purchases!"
        )

    @staticmethod
    async def process_referral(user_id: int, ref_code: str, db_session):
        if not ref_code.startswith("ref_"):
            return False
            
        referrer_id = int(ref_code.split("_")[1])
        if referrer_id == user_id:
            return False
            
        # Create referral relationship
        referral = Referral(
            user_id=user_id,
            referrer_id=referrer_id
        )
        db_session.add(referral)
        db_session.commit()
        return True