import pytest
from unittest.mock import AsyncMock, MagicMock
from handlers.product_handler import ProductHandler

@pytest.mark.asyncio
async def test_display_product():
    # Mock update and context
    update = AsyncMock()
    context = MagicMock()
    
    # Set up test data
    update.effective_user.language_code = 'en'
    context.args = ['1']
    
    # Execute test
    await ProductHandler.display_product(update, context)
    
    # Verify response
    update.message.reply_text.assert_called_once()