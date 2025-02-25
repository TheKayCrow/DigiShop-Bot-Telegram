from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
import hashlib

class ReferralUser(Base):
    __tablename__ = 'referral_users'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    referral_code = Column(String, unique=True)
    total_earnings = Column(Float, default=0.0)
    is_banned = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Anti-abuse measures
    last_referral = Column(DateTime)
    daily_referrals = Column(Integer, default=0)
    suspicious_activity = Column(Boolean, default=False)
    
    referrals = relationship("ReferralTransaction", back_populates="referrer")

class ReferralTransaction(Base):
    __tablename__ = 'referral_transactions'
    
    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer, ForeignKey('referral_users.id'))
    referred_id = Column(Integer, ForeignKey('users.id'))
    casino_id = Column(String)
    amount = Column(Float)
    status = Column(String, default='pending')  # pending, verified, rejected
    ip_address = Column(String)
    device_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    verified_at = Column(DateTime)