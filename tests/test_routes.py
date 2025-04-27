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

def test_add_task_with_title():
    app = create_app()
    client = app.test_client()
    response = client.post('/tasks', json={"title": "Nova tarefa"})
    assert response.status_code == 201

def test_update_task_status():
    app = create_app()
    client = app.test_client()
    # Primeiro cria uma tarefa
    post_response = client.post('/tasks', json={"title": "Tarefa para atualizar"})
    task_id = post_response.get_json().get("id")
    # Depois tenta atualizar
    put_response = client.put(f'/tasks/{task_id}')
    assert put_response.status_code == 200

def test_update_nonexistent_task():
    app = create_app()
    client = app.test_client()
    # Tenta atualizar uma tarefa que não existe
    response = client.put('/tasks/9999')
    assert response.status_code == 404
