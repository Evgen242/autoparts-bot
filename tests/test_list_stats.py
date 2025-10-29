import pytest
from bot import list_parts, stats


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
    def __init__(self):
        self.args = []


# Заглушка для AutoPart
class DummyPart:
    def __init__(
        self, name="Тормозной диск", brand="Toyota", model="Camry", qty=2, price=4500
    ):
        self.name = name
        self.car_brand = brand
        self.car_model = model
        self.quantity = qty
        self.price = price
        self.part_number = "43512-06060"
        self.location = "Стеллаж А1"
        self.description = "Новый"


# Заглушка для сессии
class DummySession:
    def __init__(self, parts=None, stats=None):
        self._parts = parts or []
        self._stats = stats or {}

    def query(self, *args, **kwargs):
        return self

    def all(self):
        return self._parts

    def count(self):
        return self._stats.get("count", 0)

    def scalar(self):
        return self._stats.get("scalar", 0)

    def distinct(self):
        return self

    def close(self):
        pass


@pytest.mark.asyncio
async def test_list_parts_empty(monkeypatch):
    update = DummyUpdate()
    context = DummyContext()

    monkeypatch.setattr("bot.db.Session", lambda: DummySession([]))

    await list_parts(update, context)

    assert "База данных пуста" in update.message.sent_texts[0]


@pytest.mark.asyncio
async def test_list_parts_with_data(monkeypatch):
    update = DummyUpdate()
    context = DummyContext()

    parts = [
        DummyPart(),
        DummyPart(name="Фильтр", brand="Nissan", model="X-Trail", qty=1, price=1200),
    ]
    monkeypatch.setattr("bot.db.Session", lambda: DummySession(parts))

    await list_parts(update, context)

    assert "Всего запчастей: 2" in update.message.sent_texts[0]
    assert "Тормозной диск" in update.message.sent_texts[0]
    assert "Фильтр" in update.message.sent_texts[0]


@pytest.mark.asyncio
async def test_stats(monkeypatch):
    update = DummyUpdate()
    context = DummyContext()

    stats_data = {"count": 2, "scalar": 5}
    monkeypatch.setattr("bot.db.Session", lambda: DummySession(stats=stats_data))

    await stats(update, context)

    text = update.message.sent_texts[0]
    assert "Статистика" in text
    assert "Всего позиций" in text
