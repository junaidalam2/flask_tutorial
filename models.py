from extensions import db

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120))
    salary = db.Column(db.String(50))

    def __repr__(self):
        return f"<Job {self.title}>"