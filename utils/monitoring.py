import time
from functools import wraps
from prometheus_client import Summary, Counter

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
COMMAND_COUNTER = Counter('bot_commands_total', 'Total commands processed')

def monitor_performance(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            REQUEST_TIME.observe(time.time() - start_time)
            COMMAND_COUNTER.inc()
            return result
        except Exception as e:
            # Log error and timing
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    return wrapper