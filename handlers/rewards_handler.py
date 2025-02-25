class RewardsHandler:
    @staticmethod
    async def show_rewards(update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            user_id = update.effective_user.id
            db = context.bot_data.get('db')
            stats = PartnerStats.get_user_stats(user_id, db)

            message = f"""
🎁 *Partner Rewards*

📊 *Today's Performance:*
• Earnings: `${stats['daily_earnings']:.2f}`
• Active Casinos: `{stats['active_casinos']}`
• Best Casino: `{stats['best_performing'][0] if stats['best_performing'] else 'None'}`

💎 *Available Rewards:*
• Volume Bonus: `+5%`
• Loyalty Points: `{user.wallet.bonus_points}`
• Special Access: `{'🟢 Active' if stats['daily_earnings'] > 100 else '🔴 Inactive'}`

🎯 *Next Tier:*
Progress: `{get_progress_bar(stats['daily_earnings'])}`
"""
            keyboard = [
                [
                    InlineKeyboardButton("🎰 Casino List", callback_data="show_casinos"),
                    InlineKeyboardButton("📈 Statistics", callback_data="detailed_stats")
                ],
                [InlineKeyboardButton("🔙 Back", callback_data="main_panel")]
            ]

            await update.message.reply_text(
                text=message,
                reply_markup=InlineKeyboardMarkup(keyboard),
                parse_mode='MarkdownV2'
            )

        except Exception as e:
            logger.error(f"Rewards display error: {str(e)}")