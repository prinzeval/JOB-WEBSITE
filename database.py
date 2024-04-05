from sqlalchemy import create_engine, text
import security

engine = create_engine(security.sql_pass)

with engine.connect() as conn:
    dict_list = []
    result = conn.execute(text("SELECT * FROM jobs"))  
    All_result = result.fetchall()
    colunm_result = result.keys()
    dict_result =[dict(zip(colunm_result,row))for row in All_result]
    dict_list.append(dict_result)



def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
         
        All_result = result.fetchall()
        colunm_result = result.keys()
        dict_result =[dict(zip(colunm_result,row))for row in All_result]
        
        return dict_result   
