from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route('/')
def helen():
    my_jobs = load_jobs_from_db()
    return render_template('home.html', jobs=my_jobs, company_name='VALENDATA')

@app.route("/api/jobs")
def list_jobs():
    my_jobs = load_jobs_from_db()
    return jsonify(my_jobs)

@app.route("/job/<int:id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "NOT FOUND", 404
    return render_template('jobpage.html', job=job)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
