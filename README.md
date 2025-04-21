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
