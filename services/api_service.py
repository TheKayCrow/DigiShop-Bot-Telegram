from abc import ABC, abstractmethod
import aiohttp
from config.api_config import APIConfig

class StoreAPI(ABC):
    @abstractmethod
    async def search_products(self, query: str, category: str = None):
        pass
    
    @abstractmethod
    async def get_product_details(self, product_id: str):
        pass

class AmazonAPI(StoreAPI):
    def __init__(self, config: APIConfig):
        self.api_key = config.AMAZON_API_KEY
        self.secret_key = config.AMAZON_SECRET_KEY
        
    async def search_products(self, query: str, category: str = None):
        # Implement Amazon API search
        pass

class EbayAPI(StoreAPI):
    def __init__(self, config: APIConfig):
        self.api_key = config.EBAY_API_KEY
        
    async def search_products(self, query: str, category: str = None):
        # Implement eBay API search
        pass