import os
import pytest

def test_env_vars_present():
    for key in ("POSTGRES_USER", "POSTGRES_PASSWORD", "POSTGRES_DB", "POSTGRES_HOST"):
        assert key in os.environ, f"Missing env {key}"

@pytest.mark.skip(reason="Enable when real DB test is ready")
def test_db_connection_placeholder():
    assert True
