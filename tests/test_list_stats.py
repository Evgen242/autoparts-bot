from bot import list_parts, stats
from telegram import Update
from unittest.mock import AsyncMock


def test_list_parts_command():
    update = AsyncMock(Update)
    context = AsyncMock()
    update.message.reply_text = AsyncMock()

    # Import and test
    import asyncio

    asyncio.run(list_parts(update, context))
    assert update.message.reply_text.called


def test_stats_command():
    update = AsyncMock(Update)
    context = AsyncMock()
    update.message.reply_text = AsyncMock()

    # Import and test
    import asyncio

    asyncio.run(stats(update, context))
    assert update.message.reply_text.called
