from typing import Dict
from database.models import User, ReferralTransaction
from datetime import datetime, timedelta

class PartnerStats:
    @staticmethod
    def get_user_stats(user_id: int, db) -> Dict:
        now = datetime.utcnow()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)

        stats = {
            "daily_earnings": 0.0,
            "total_referrals": 0,
            "active_casinos": 0,
            "best_performing": None
        }

        transactions = db.query(ReferralTransaction).filter(
            ReferralTransaction.referrer_id == user_id,
            ReferralTransaction.created_at >= start_of_day
        ).all()

        # Calculate statistics
        if transactions:
            stats["daily_earnings"] = sum(t.amount for t in transactions)
            stats["active_casinos"] = len(set(t.casino_id for t in transactions))
            
            # Get best performing casino
            casino_earnings = {}
            for t in transactions:
                casino_earnings[t.casino_id] = casino_earnings.get(t.casino_id, 0) + t.amount
            
            if casino_earnings:
                stats["best_performing"] = max(casino_earnings.items(), key=lambda x: x[1])

        return stats