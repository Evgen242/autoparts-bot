import pytest
import types
from bot import add_part_process, main_keyboard


# Заглушка для update.message
class DummyMessage:
    def __init__(self, text=""):
        self.text = text
        self.sent_texts = []
        self.reply_markup = None

    async def reply_text(self, text, reply_markup=None):
        self.sent_texts.append(text)
        self.reply_markup = reply_markup
        return text


class DummyUpdate:
    def __init__(self, text):
        self.message = DummyMessage(text)


class DummyContext:
    def __init__(self):
        self.args = []


# Заглушка для db.Session
class DummySession:
    def __init__(self):
        self.added = []
        self.committed = False

    def add(self, obj):
        self.added.append(obj)

    def commit(self):
        self.committed = True

    def close(self):
        pass


@pytest.mark.asyncio
async def test_add_part_not_enough_data(monkeypatch):
    update = DummyUpdate("Только одна строка")
    context = DummyContext()

    # Подменяем db.Session на заглушку
    monkeypatch.setattr("bot.db.Session", lambda: DummySession())

    result = await add_part_process(update, context)

    assert "Недостаточно данных" in update.message.sent_texts[0]
    assert result == 1  # ADD_PART state


@pytest.mark.asyncio
async def test_add_part_success(monkeypatch):
    valid_input = """Тормозной диск
Toyota
Camry
43512-06060
2
4500
Стеллаж А1
Новый, оригинал"""
    update = DummyUpdate(valid_input)
    context = DummyContext()

    dummy_session = DummySession()
    monkeypatch.setattr("bot.db.Session", lambda: dummy_session)

    result = await add_part_process(update, context)

    assert "успешно добавлена" in update.message.sent_texts[0]
    assert dummy_session.committed is True
    assert result == -1  # ConversationHandler.END
