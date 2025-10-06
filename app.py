from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, jsonify
from config import Config
from extensions import db, migrate
from models import Job  


def create_app():
      app = Flask(__name__)
      app.config.from_object(Config)

      db.init_app(app)
      migrate.init_app(app, db)

      @app.route("/")
      def hello_world():
            jobs = Job.query.all()
            return render_template('home.html', jobs=jobs)

      @app.route("/api/jobs")
      def list_jobs():
            jobs = Job.query.all()
            jobs_list = [
                  {
                  "id": job.id,
                  "title": job.title,
                  "location": job.location,
                  "salary": job.salary,
                  } for job in jobs
            ]
            return jsonify(jobs_list)

      return app


if __name__ == "__main__":
        app = create_app()
        app.run(host='0.0.0.0', debug=True)



      # JOBS = [
      # {
      #       'id': 1,
      #       'title': 'Data Analyst',
      #       'salary': '120, 000'
      # },
      # {
      #       'id': 2,
      #       'title': 'Data Scientist',
      #       'location': 'San Francisco, California',
      #       'salary': '190, 000'
      # },
      # {
      #       'id': 3,
      #       'title': 'Junior Software Engineer',
      #       'location': 'New York, New York',
      #       'salary': '160, 000'
      # },
      # {
      #       'id': 4,
      #       'title': 'Software Architect Engineer',
      #       'location': 'Houston, Texas',
      # },
      # ]