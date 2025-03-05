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
    response = client.post('/start_timer', json={'duration': 25}) # Assuming 25 minutes work
    assert response.status_code == 200
    assert response.json['status'] == 'timer_started'
    pass

def test_short_break(client):
    response = client.post('/start_break', json={'duration': 5}) # Assuming 5 minutes break
    assert response.status_code == 200
    assert response.json['status'] == 'break_started'
    pass

def test_long_break(client):
    response = client.post('/start_break', json={'duration': 15}) # Assuming 15 minutes break
    assert response.status_code == 200
    assert response.json['status'] == 'break_started'
    pass
