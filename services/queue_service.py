from celery import Celery
from typing import Dict, Any

celery_app = Celery('digishop', broker='redis://localhost:6379/1')

@celery_app.task
def process_casino_registration(user_data: Dict[str, Any]):
    # Process registration in background
    pass

@celery_app.task
def update_statistics():
    # Update stats in background
    pass