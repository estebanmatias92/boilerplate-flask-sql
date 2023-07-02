from flask import Flask
from routes.todo import todo_route
from db.database import init_db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo_route)
    init_db(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
