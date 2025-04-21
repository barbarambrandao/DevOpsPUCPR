from app import create_app

def test_get_tasks():
    app = create_app()
    client = app.test_client()

    response = client.get('/tasks')
    assert response.status_code == 200

def test_add_task_without_title():
    app = create_app()
    client = app.test_client()
    response = client.post('/tasks', json={})
    assert response.status_code == 400
