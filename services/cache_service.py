from redis import Redis
from typing import Any
import json

class CacheService:
    def __init__(self):
        self.redis = Redis(host='localhost', port=6379, db=0, decode_responses=True)
        self.default_ttl = 3600  # 1 hour

    async def get_cached_data(self, key: str) -> Any:
        data = self.redis.get(key)
        return json.loads(data) if data else None

    async def set_cached_data(self, key: str, value: Any, ttl: int = None):
        self.redis.set(key, json.dumps(value), ex=ttl or self.default_ttl)