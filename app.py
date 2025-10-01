from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
      app = Flask(__name__)
      app.config.from_object(Config)

      db.init_app(app)
      migrate.init_app(app, db)

      JOBS = [
      {
            'id': 1,
            'title': 'Data Analyst',
            'salary': '120, 000'
      },
      {
            'id': 2,
            'title': 'Data Scientist',
            'location': 'San Francisco, California',
            'salary': '190, 000'
      },
      {
            'id': 3,
            'title': 'Junior Software Engineer',
            'location': 'New York, New York',
            'salary': '160, 000'
      },
      {
            'id': 4,
            'title': 'Software Architect Engineer',
            'location': 'Houston, Texas',
      },
      ]

      @app.route("/")
      def hello_world():
            return render_template('home.html', jobs=JOBS)

      @app.route('/api/jobs')
      def list_jobs():
            return jsonify(JOBS)

if __name__ == "__main__":
        app = create_app()
        app.run(host='0.0.0.0', debug=True)
