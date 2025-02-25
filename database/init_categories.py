from sqlalchemy.orm import Session
from database.models import Category
from database.categories_data import SHOP_CATEGORIES
from database.connection import get_db

def init_categories(db: Session):
    try:
        # Add main categories
        for main_category, subcategories in SHOP_CATEGORIES.items():
            # Check if main category exists
            main_cat = db.query(Category).filter_by(name=main_category).first()
            if not main_cat:
                main_cat = Category(name=main_category)
                db.add(main_cat)
                db.flush()  # Get the ID of the main category
                
                # Add subcategories
                for sub_category in subcategories:
                    sub_cat = Category(
                        name=sub_category,
                        parent_id=main_cat.id
                    )
                    db.add(sub_cat)
        
        db.commit()
        print("Categories initialized successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"Error initializing categories: {str(e)}")
        raise