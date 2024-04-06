from sqlalchemy import create_engine, text

username = "root"
password = "Vondabaic2020"
hostname = "127.0.0.1"
port = "3306"
database = "val_data"

# Create the SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}")
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
