from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
          'id': 1,
          'title': 'Data Analyst',
          'location': 'San Francisco, California',
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
        app.run(host='0.0.0.0', debug=True)
