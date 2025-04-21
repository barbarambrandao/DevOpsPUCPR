# To-Do List API

API simples para gerenciar tarefas.

## Como executar

```bash
pip install -r requirements.txt
python run.py


**`app/__init__.py`**
```python
from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import bp
    app.register_blueprint(bp)
    return app

## Rotas disponíveis

- `GET /tasks`: Lista todas as tarefas
- `POST /tasks`: Adiciona uma nova tarefa (JSON: `{ "title": "Nome da tarefa" }`)
- `PUT /tasks/<id>`: Marca a tarefa como feita

