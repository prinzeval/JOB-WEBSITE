from flask import Flask, render_template,jsonify
from database import engine,load_jobs_from_db,load_job_from_db
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

@app.route("/job/<id>") 
def show_job(id):  
    job = load_job_from_db(id)

    if not job:
        return "NOT FOUND", 404
    
    return render_template('jobpage.html', job=job)



if __name__ == '__main__': 
    app.run(host = '0.0.0.0', debug=True)







# from flask import Flask,jsonify,request
# from flask_sqlalchemy import SQLAlchemy
# # from database import 

# # Initialize Flask application
# app = Flask(__name__)
# # Configure the SQLite database URI
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# # Initialize SQLAlchemy extension
# db = SQLAlchemy(app)

# # Define your model
# class Drink(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     description = db.Column(db.String(100))

#     def __repr__(self):
#         return f"{self.name} - {self.description}"

# # Create the database tables within the application context
# with app.app_context():
#     db.create_all()

# # Define your routes
# @app.route('/')
# def index():
#     return "hello!"

# @app.route('/drinks')
# def get_drinks():
#     ALL = Drink.query.all()
#     output = []
#     for drinks in ALL:
#         drink_data = {"name":drinks.name,"description":drinks.description}
#         output.append(drink_data)
#     return {"drink": output}

# @app.route('/drinks/<id>')
# def get_drink(id):  
#     DD = Drink.query.get(id)
#     if not DD:
#         return "NOT FOUND", 404
    
#     return jsonify({"name":DD.name,"description":DD.description})

# @app.route('/drinks', methods=['POST'])
# def add_drink():
   
#     drink = Drink(name=request.json['name'], description=request.json['description'])
#     db.session.add(drink)
#     db.session.commit()
#     return {'id': drink.id}
# @app.route('/drinks/<id>', methods = ['DELETE'])
# def delete_drink(id):
#     drink = Drink.query.get(id)
#     if drink:
#         db.session.delete(drink)
#         db.session.commit()
#         return{"message":"yeet!@"}
#     else:
#         return "404 NOT_FOUND"

# # Run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)




