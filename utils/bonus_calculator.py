def calculate_bonus(amount: float) -> float:
    """Calculate deposit bonus based on amount"""
    if amount >= 500:
        return amount * 0.20  # 20% bonus
    elif amount >= 200:
        return amount * 0.15  # 15% bonus
    elif amount >= 100:
        return amount * 0.10  # 10% bonus
    elif amount >= 50:
        return amount * 0.05  # 5% bonus
    return 0.0

def get_tier_emoji(balance: float) -> str:
    """Get user tier emoji based on balance"""
    if balance >= 500:
        return "👑 Diamond"
    elif balance >= 200:
        return "💎 Platinum"
    elif balance >= 100:
        return "🥇 Gold"
    elif balance >= 50:
        return "🥈 Silver"
    return "🥉 Bronze"