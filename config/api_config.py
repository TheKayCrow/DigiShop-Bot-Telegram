from pydantic import BaseSettings

class APIConfig(BaseSettings):
    # Store 1 - Example: Amazon
    AMAZON_API_KEY: str
    AMAZON_SECRET_KEY: str
    AMAZON_REGION: str

    # Store 2 - Example: eBay
    EBAY_API_KEY: str
    EBAY_CLIENT_ID: str

    # Store 3 - Example: AliExpress
    ALIEXPRESS_API_KEY: str
    ALIEXPRESS_SECRET: str

    class Config:
        env_file = '.env'