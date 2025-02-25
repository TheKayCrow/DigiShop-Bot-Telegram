from typing import Dict

PERFORMANCE_CONFIG: Dict = {
    "cache_ttl": {
        "commands": 300,      # 5 minutes
        "casino_list": 600,   # 10 minutes
        "user_data": 60,      # 1 minute
        "statistics": 1800    # 30 minutes
    },
    "thread_pool": {
        "max_workers": 10,
        "queue_size": 100
    },
    "database": {
        "pool_size": 20,
        "max_overflow": 10,
        "pool_timeout": 30
    },
    "rate_limits": {
        "commands_per_minute": 30,
        "messages_per_second": 1
    }
}