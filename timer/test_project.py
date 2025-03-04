import pytest
from project import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_main_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_timer_start(client):
    # Add test logic for timer start
    pass

def test_short_break(client):
    # Add test logic for short break
    pass

def test_long_break(client):
    # Add test logic for long break
    pass
