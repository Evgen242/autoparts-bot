import pytest
from bot import start, add_part_process, search_part, list_parts, stats, main_keyboard

# ==== Общие заглушки ====
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
    def __init__(self, text=""):
        self.message = DummyMessage(text)

class DummyContext:
    def __init__(self, args=None):
        self.args = args or []

# ==== Заглушки для базы ====
class DummyPart:
    def __init__(self, name="Тормозной диск", brand="Toyota", model="Camry", qty=2, price=4500):
        self.name = name
        self.car_brand = brand
        self.car_model = model
        self.part_number = "43512-06060"
        self.quantity = qty
        self.price = price
        self.location = "Стеллаж А1"
        self.description = "Новый"

class DummySession:
    def __init__(self, parts=None, stats=None):
        self._parts = parts or []
        self._stats = stats or {}
        self.added = []
        self.committed = False
    def add(self, obj): self.added.append(obj)
    def commit(self): self.committed = True
    def close(self): pass
    def query(self, *args, **kwargs): return self
    def filter(self, *args, **kwargs): return self
    def all(self): return self._parts
    def count(self): return self._stats.get("count", 0)
    def scalar(self): return self._stats.get("scalar", 0)
    def distinct(self): return self

# ==== Тесты ====

@pytest.mark.asyncio
async def test_start_handler():
    update, context = DummyUpdate(), DummyContext()
    await start(update, context)
    assert "Добро пожаловать" in update.message.sent_texts[0]
    assert update.message.reply_markup == main_keyboard

@pytest.mark.asyncio
async def test_add_part_not_enough_data(monkeypatch):
    update, context = DummyUpdate("Только одна строка"), DummyContext()
    monkeypatch.setattr("bot.db.Session", lambda: DummySession())
    result = await add_part_process(update, context)
    assert "Недостаточно данных" in update.message.sent_texts[0]
    assert result == 1  # ADD_PART

@pytest.mark.asyncio
async def test_add_part_success(monkeypatch):
    valid_input = """Тормозной диск
Toyota
Camry
43512-06060
2
4500
Стеллаж А1
Новый"""
    update, context = DummyUpdate(valid_input), DummyContext()
    dummy_session = DummySession()
    monkeypatch.setattr("bot.db.Session", lambda: dummy_session)
    result = await add_part_process(update, context)
    assert "успешно добавлена" in update.message.sent_texts[0]
    assert dummy_session.committed is True
    assert result == -1  # ConversationHandler.END

@pytest.mark.asyncio
async def test_search_no_results(monkeypatch):
    update, context = DummyUpdate(), DummyContext(args=["Camry"])
    monkeypatch.setattr("bot.db.Session", lambda: DummySession([]))
    await search_part(update, context)
    assert "Ничего не найдено" in update.message.sent_texts[0]

@pytest.mark.asyncio
async def test_search_with_results(monkeypatch):
    update, context = DummyUpdate(), DummyContext(args=["Camry"])
    monkeypatch.setattr("bot.db.Session", lambda: DummySession([DummyPart()]))
    await search_part(update, context)
    assert "Найдено запчастей" in update.message.sent_texts[0]
    assert "Toyota Camry" in update.message.sent_texts[0]

@pytest.mark.asyncio
async def test_list_parts_empty(monkeypatch):
    update, context = DummyUpdate(), DummyContext()
    monkeypatch.setattr("bot.db.Session", lambda: DummySession([]))
    await list_parts(update, context)
    assert "База данных пуста" in update.message.sent_texts[0]

@pytest.mark.asyncio
async def test_list_parts_with_data(monkeypatch):
    update, context = DummyUpdate(), DummyContext()
    parts = [DummyPart(), DummyPart(name="Фильтр", brand="Nissan", model="X-Trail", qty=1, price=1200)]
    monkeypatch.setattr("bot.db.Session", lambda: DummySession(parts))
    await list_parts(update, context)
    text = update.message.sent_texts[0]
    assert "Всего запчастей: 2" in text
    assert "Тормозной диск" in text
    assert "Фильтр" in text

@pytest.mark.asyncio
async def test_stats(monkeypatch):
    update, context = DummyUpdate(), DummyContext()
    stats_data = {"count": 2, "scalar": 5}
    monkeypatch.setattr("bot.db.Session", lambda: DummySession(stats=stats_data))
    await stats(update, context)
    text = update.message.sent_texts[0]
    assert "Статистика" in text
    assert "Всего позиций" in text
