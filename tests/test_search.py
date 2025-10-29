import pytest
from bot import search_part


class DummyMessage:
    def __init__(self):
        self.sent_texts = []

    async def reply_text(self, text, reply_markup=None):
        self.sent_texts.append(text)
        return text


class DummyUpdate:
    def __init__(self):
        self.message = DummyMessage()


class DummyContext:
    def __init__(self, args=None):
        self.args = args or []


# Заглушка для объекта AutoPart
class DummyPart:
    def __init__(
        self,
        name="Тормозной диск",
        brand="Toyota",
        model="Camry",
        number="43512-06060",
        qty=2,
        price=4500,
        loc="Стеллаж А1",
        desc="Новый",
    ):
        self.name = name
        self.car_brand = brand
        self.car_model = model
        self.part_number = number
        self.quantity = qty
        self.price = price
        self.location = loc
        self.description = desc


# Заглушка для сессии
class DummySession:
    def __init__(self, results):
        self._results = results

    def query(self, *args, **kwargs):
        return self

    def filter(self, *args, **kwargs):
        return self

    def all(self):
        return self._results

    def close(self):
        pass


@pytest.mark.asyncio
async def test_search_no_results(monkeypatch):
    update = DummyUpdate()
    context = DummyContext(args=["Camry"])

    monkeypatch.setattr("bot.db.Session", lambda: DummySession([]))

    await search_part(update, context)

    assert "Ничего не найдено" in update.message.sent_texts[0]


@pytest.mark.asyncio
async def test_search_with_results(monkeypatch):
    update = DummyUpdate()
    context = DummyContext(args=["Camry"])

    dummy_part = DummyPart()
    monkeypatch.setattr("bot.db.Session", lambda: DummySession([dummy_part]))

    await search_part(update, context)

    assert "Найдено запчастей" in update.message.sent_texts[0]
    assert "Toyota Camry" in update.message.sent_texts[0]
