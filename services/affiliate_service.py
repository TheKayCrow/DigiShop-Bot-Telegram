from typing import Dict, List

class AffiliateService:
    CASINO_PROGRAMS: Dict[str, Dict] = {
        "stake": {
            "name": "Stake.com",
            "commission": "40%",
            "min_deposit": "10 USDT",
            "bonus": "200% First Deposit",
            "aff_link": "stake.com/?c=yourid"
        },
        "roobet": {
            "name": "Roobet",
            "commission": "45%",
            "min_deposit": "5 USDT",
            "bonus": "Daily Rakeback",
            "aff_link": "roobet.com/?ref=yourid"
        }
        # Add other casinos similarly
    }

    EARNING_PROGRAMS: Dict[str, Dict] = {
        "surveys": {
            "name": "Survey Platform",
            "commission": "30%",
            "min_payout": "5 USDT",
            "earning_potential": "$100-500/month",
            "aff_link": "surveys.com/?ref=yourid"
        },
        "microtasks": {
            "name": "Micro Tasks",
            "commission": "25%",
            "min_payout": "3 USDT",
            "earning_potential": "$50-300/month",
            "aff_link": "tasks.com/?ref=yourid"
        }
        # Add other programs similarly
    }