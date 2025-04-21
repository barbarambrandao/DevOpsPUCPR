from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes import bp
    app.register_blueprint(bp)
    return app

# 🔽 Adicione isso no final:
__all__ = ["create_app"]
