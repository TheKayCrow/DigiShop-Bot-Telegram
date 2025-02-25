CREATE TABLE referral_users (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    referral_code VARCHAR(50) UNIQUE,
    total_earnings DECIMAL(10,2) DEFAULT 0,
    is_banned BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_referral TIMESTAMP,
    daily_referrals INTEGER DEFAULT 0,
    suspicious_activity BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_referral_code ON referral_users(referral_code);