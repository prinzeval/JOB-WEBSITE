from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:Vondabaic2020@localhost/val_data")

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM job_postings"))
         
        All_result = result.fetchall()
        colunm_result = result.keys()
        dict_result =[dict(zip(colunm_result,row))for row in All_result]
        return dict_result   
    
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM job_postings WHERE id = :val").bindparams(val=id)
        )
        rows = result.fetchall()
        if len(rows) == 0:
            return None
        else:
            # Construct a list of dictionaries for each row
            return [{key: value for key, value in zip(result.keys(), row)} for row in rows]