from bot import start
from telegram import Update
from unittest.mock import AsyncMock


def test_start_command():
    update = AsyncMock(Update)
    context = AsyncMock()

    # Mock user data
    update.effective_user.id = 12345
    update.message.reply_text = AsyncMock()

    # Import and test
    import asyncio

    asyncio.run(start(update, context))

    # Check if reply was called
    assert update.message.reply_text.called
