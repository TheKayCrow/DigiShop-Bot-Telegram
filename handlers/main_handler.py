from services.cache_service import CacheService
from concurrent.futures import ThreadPoolExecutor

class MainHandler:
    def __init__(self):
        self.cache = CacheService()
        self.executor = ThreadPoolExecutor(max_workers=10)

    async def handle_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        cache_key = f"cmd_{update.effective_user.id}_{update.message.text}"
        
        # Try to get from cache first
        cached_response = await self.cache.get_cached_data(cache_key)
        if cached_response:
            await update.message.reply_text(**cached_response)
            return

        # Process command in thread pool
        response = await self.process_command_async(update, context)
        await self.cache.set_cached_data(cache_key, response, ttl=300)  # 5 minutes cache