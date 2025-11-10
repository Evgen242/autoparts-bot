from database import init_db


def test_database_connection():
    # Test that init_db doesn't crash
    try:
        init_db()
        assert True
    except Exception:
        assert False, "Database initialization failed"
