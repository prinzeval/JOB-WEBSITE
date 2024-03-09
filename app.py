from flask import Flask, render_template,jsonify


app = Flask(__name__)
JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Newyork NY, USA',
        'salary':  '$2,000'
    },
      {
        'id':2,
        'title': 'Data Scienstist',
        'location': 'California, Usa',
        

    },
      {
        'id':3,
        'title': 'Monkey analyst',
        'location': 'Remote',
        'salary':  '$150,000'
    },
      {
        'id':4,
        'title': 'Data Entry Clerk',
        'location': 'Ontario, Canada',
        'salary':  '$5,000'
    },
]
@app.route('/')
def helen():
    return render_template('home.html',
                           jobs = JOBS,
                           company_name = 'Meta')
@app.route("/jobs")


def list_jobs ():
    return jsonify(JOBS)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)




