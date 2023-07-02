from db.database import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), unique=True, nullable=False)
    is_done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Todo %r>' % self.task
