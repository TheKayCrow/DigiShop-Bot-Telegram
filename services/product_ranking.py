from sqlalchemy.orm import Session
from database.models import Product
from typing import List

class ProductRanking:
    @staticmethod
    def get_best_price_product(db: Session, similar_products: List[Product]) -> Product:
        return min(similar_products, key=lambda p: p.price)

    @staticmethod
    def get_top_products(db: Session, limit: int = 10) -> List[Product]:
        return db.query(Product)\
            .filter(Product.is_top == True)\
            .order_by(Product.sales_count.desc())\
            .limit(limit)\
            .all()

    @staticmethod
    def get_best_sellers(db: Session, limit: int = 10) -> List[Product]:
        return db.query(Product)\
            .order_by(Product.sales_count.desc())\
            .limit(limit)\
            .all()