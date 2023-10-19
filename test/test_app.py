from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data

def test_about():
    client = app.test_client()
    response = client.get('/about')
    assert response.status_code == 200
    assert b'This is Ankeet Chauhan.' in response.data

