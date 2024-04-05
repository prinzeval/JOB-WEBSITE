from flask import Flask, render_template,jsonify
from database import engine,load_jobs_from_db
from sqlalchemy import text


app = Flask(__name__)



@app.route('/')
def helen():
    my_jobs = load_jobs_from_db()
    return render_template('home.html',
                           jobs = my_jobs,
                           company_name = 'Meta')

@app.route("/api/jobs")
def list_jobs ():
    my_jobs = load_jobs_from_db()
    return jsonify(my_jobs)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)

