from datetime import datetime, timedelta
import hashlib
from typing import Tuple

class AntiAbuseService:
    MAX_DAILY_REFERRALS = 10
    MIN_TIME_BETWEEN_REFERRALS = timedelta(minutes=30)
    
    @staticmethod
    def check_referral_validity(user: ReferralUser, ip: str, device_info: str) -> Tuple[bool, str]:
        now = datetime.utcnow()
        
        # Check if banned
        if user.is_banned:
            return False, "User is banned from referral system"
            
        # Check daily limit
        if user.daily_referrals >= AntiAbuseService.MAX_DAILY_REFERRALS:
            return False, "Daily referral limit reached"
            
        # Check time between referrals
        if user.last_referral:
            time_diff = now - user.last_referral
            if time_diff < AntiAbuseService.MIN_TIME_BETWEEN_REFERRALS:
                return False, "Please wait between referrals"
                
        # Check IP and device repetition
        device_hash = hashlib.sha256(device_info.encode()).hexdigest()
        
        return True, "Valid referral"

    @staticmethod
    def verify_casino_registration(transaction: ReferralTransaction) -> bool:
        # Implement casino API verification here
        pass