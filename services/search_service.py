from typing import List
from sqlalchemy import or_
from database.models import Product

class SearchService:
    @staticmethod
    def search_products(db, query: str, filters: dict = None) -> List[Product]:
        search_query = db.query(Product).filter(
            or_(
                Product.name.ilike(f"%{query}%"),
                Product.description.ilike(f"%{query}%")
            )
        )
        
        if filters:
            if 'min_price' in filters:
                search_query = search_query.filter(Product.price >= filters['min_price'])
            if 'max_price' in filters:
                search_query = search_query.filter(Product.price <= filters['max_price'])
            if 'category' in filters:
                search_query = search_query.filter(Product.category_id == filters['category'])
                
        return search_query.limit(10).all()