from decimal import Decimal

class CryptoBonus:
    @staticmethod
    def calculate_deposit_bonus(amount: float, crypto_type: str) -> float:
        """Calculate bonus percentage based on crypto type and amount"""
        base_bonus = {
            'BTC': 0.25,  # 25% base bonus for BTC
            'ETH': 0.20,  # 20% base bonus for ETH
            'USDT': 0.15  # 15% base bonus for USDT
        }
        
        # Additional bonus for larger deposits
        volume_bonus = 0.0
        if amount >= 0.1 and crypto_type == 'BTC':
            volume_bonus = 0.10
        elif amount >= 1.0 and crypto_type == 'ETH':
            volume_bonus = 0.08
        elif amount >= 100 and crypto_type == 'USDT':
            volume_bonus = 0.05
            
        return base_bonus[crypto_type] + volume_bonus