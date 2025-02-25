from sqlalchemy import text
from sqlalchemy.orm import joinedload

class OptimizedQueries:
    @staticmethod
    async def get_user_data(db, user_id: int):
        return db.query(User)\
            .options(
                joinedload(User.wallet),
                joinedload(User.referrals),
                joinedload(User.preferences)
            )\
            .filter_by(id=user_id)\
            .first()

    @staticmethod
    async def get_active_casinos(db):
        # Use raw SQL for better performance
        sql = text("""
            SELECT c.*, COUNT(t.id) as transactions
            FROM casinos c
            LEFT JOIN casino_transactions t ON c.id = t.casino_id
            WHERE c.is_active = true
            GROUP BY c.id
            ORDER BY transactions DESC
            LIMIT 10
        """)
        return db.execute(sql).fetchall()