from datetime import datetime
from database.models import AffiliateClick, CasinoRegistration

class TrackingService:
    @staticmethod
    async def track_casino_click(user_id: int, casino_id: str, db_session):
        try:
            click = AffiliateClick(
                user_id=user_id,
                casino_id=casino_id,
                clicked_at=datetime.utcnow()
            )
            db_session.add(click)
            db_session.commit()
            
        except Exception as e:
            db_session.rollback()
            logger.error(f"Click tracking error: {str(e)}")