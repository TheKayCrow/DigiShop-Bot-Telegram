from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    preferences = relationship("UserPreferences", uselist=False, back_populates="user")
    orders = relationship("Order", back_populates="user")
    wallet = relationship("Wallet", uselist=False, back_populates="user")

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('categories.id'))
    children = relationship("Category")
    products = relationship("Product", back_populates="category")

class ProductSource(enum.Enum):
    AMAZON = "amazon"
    EBAY = "ebay"
    ALIEXPRESS = "aliexpress"
    DIRECT = "direct"

class Currency(enum.Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    JPY = "JPY"

class Language(enum.Enum):
    EN = "en"
    IT = "it"
    ES = "es"
    FR = "fr"
    DE = "de"

class CryptoType(enum.Enum):
    BTC = "BTC"
    ETH = "ETH"
    USDT = "USDT"

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(Enum(Currency), default=Currency.USD)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    source = Column(Enum(ProductSource))
    external_id = Column(String)  # ID from external store
    stock = Column(Integer, default=0)
    sales_count = Column(Integer, default=0)
    rating = Column(Float, default=0.0)
    is_top = Column(Boolean, default=False)
    is_featured = Column(Boolean, default=False)
    category = relationship("Category", back_populates="products")

class Referral(Base):
    __tablename__ = 'referrals'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    referrer_id = Column(Integer, ForeignKey('users.id'))
    commission_rate = Column(Float, default=0.05)  # 5% default
    created_at = Column(DateTime, default=datetime.utcnow)
    total_earnings = Column(Float, default=0.0)
    
    user = relationship("User", foreign_keys=[user_id])
    referrer = relationship("User", foreign_keys=[referrer_id])

class UserPreferences(Base):
    __tablename__ = 'user_preferences'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    language = Column(String)  # ISO 639-1 code
    currency = Column(String)  # ISO 4217 code
    preferred_crypto = Column(Enum(CryptoType), default=CryptoType.BTC)
    show_crypto_savings = Column(Boolean, default=True)
    user = relationship("User", back_populates="preferences")

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    total_amount = Column(Float, nullable=False)
    payment_method = Column(String)
    crypto_payment_id = Column(String, nullable=True)
    status = Column(String, default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    
    items = relationship('OrderItem', back_populates='order')
    user = relationship('User', back_populates='orders')

class Wallet(Base):
    __tablename__ = 'wallets'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    balance = Column(Float, default=0.0)
    crypto_balance = Column(Float, default=0.0)
    bonus_points = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_deposit = Column(DateTime)
    
    user = relationship('User', back_populates='wallet')

class WalletTransaction(Base):
    __tablename__ = 'wallet_transactions'
    
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    amount = Column(Float)
    type = Column(String)  # 'deposit', 'purchase', 'bonus'
    created_at = Column(DateTime, default=datetime.utcnow)

class CryptoWallet(Base):
    __tablename__ = 'crypto_wallets'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    btc_balance = Column(Float, default=0.0)
    eth_balance = Column(Float, default=0.0)
    usdt_balance = Column(Float, default=0.0)
    loyalty_points = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    transactions = relationship('CryptoTransaction', back_populates='wallet')

class CryptoTransaction(Base):
    __tablename__ = 'crypto_transactions'
    
    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('crypto_wallets.id'))
    amount = Column(Float)
    crypto_type = Column(Enum('BTC', 'ETH', 'USDT', name='crypto_types'))
    tx_hash = Column(String)
    type = Column(String)  # 'deposit', 'purchase', 'bonus'
    created_at = Column(DateTime, default=datetime.utcnow)