import pytest
from unittest.mock import AsyncMock, MagicMock
from handlers.crypto_handler import CryptoHandler

@pytest.mark.asyncio
async def test_start():
    update = AsyncMock()
    context = MagicMock()
    await CryptoHandler.start(update, context)
    update.message.reply_text.assert_called_once()