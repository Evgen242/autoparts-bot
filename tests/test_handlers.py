import pytest
from bot import start, main_keyboard

class DummyMessage:
    def __init__(self):
        self.sent_texts = []
        self.reply_markup = None

    async def reply_text(self, text, reply_markup=None):
        self.sent_texts.append(text)
        self.reply_markup = reply_markup
        return text

class DummyUpdate:
    def __init__(self):
        self.message = DummyMessage()

class DummyContext:
    def __init__(self):
        self.args = []

@pytest.mark.asyncio
async def test_start_handler():
    update = DummyUpdate()
    context = DummyContext()

    await start(update, context)

    # Проверяем, что сообщение отправлено
    assert len(update.message.sent_texts) == 1
    assert "Добро пожаловать" in update.message.sent_texts[0]
    # Проверяем, что клавиатура прикреплена
    assert update.message.reply_markup == main_keyboard
