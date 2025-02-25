def get_user_tier_emoji(user) -> str:
    if user.wallet.balance >= 1000:
        return "👑 Diamond Partner"
    elif user.wallet.balance >= 500:
        return "💎 Platinum Partner"
    elif user.wallet.balance >= 100:
        return "🥇 Gold Partner"
    return "🥈 Silver Partner"

def get_progress_bar(earnings: float) -> str:
    target = 100
    progress = min(int((earnings / target) * 10), 10)
    return f"{'▰' * progress}{'▱' * (10-progress)} {earnings:.0f}/100$"