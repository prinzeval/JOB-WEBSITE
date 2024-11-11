# from sqlalchemy import create_engine, text

# engine = create_engine("mysql+pymysql://root:Vondabaic2020@localhost/val_data")

# def load_jobs_from_db():
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT * FROM job_postings"))
         
#         All_result = result.fetchall()
#         colunm_result = result.keys()
#         dict_result =[dict(zip(colunm_result,row))for row in All_result]
#         return dict_result   
    
    
# def load_job_from_db(id):
#     with engine.connect() as conn:
#         result = conn.execute(
#             text("SELECT * FROM job_postings WHERE id = :val").bindparams(val=id)
#         )
#         rows = result.fetchall()
#         if len(rows) == 0:
#             return None
#         else:
#             # Construct a list of dictionaries for each row
#             return [{key: value for key, value in zip(result.keys(), row)} for row in rows]



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import JobListing
import os
from dotenv import load_dotenv
load_dotenv() 
# Load the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Set up the engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to load all jobs from the database
def load_jobs_from_db():
    with SessionLocal() as session:
        jobs = session.query(JobListing).all()
        return [job.__dict__ for job in jobs]

# Function to load a single job by ID from the database
def load_job_from_db(job_id):
    with SessionLocal() as session:
        job = session.query(JobListing).filter(JobListing.id == job_id).first()
        return job.__dict__ if job else None
