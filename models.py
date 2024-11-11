from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JobListing(Base):
    __tablename__ = 'Job_listing'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String, nullable=False)  # VARCHAR
    company_name = Column(String, nullable=False)  # VARCHAR
    location = Column(String, nullable=False)  # VARCHAR
    salary = Column(String, nullable=True)  # VARCHAR
    job_link = Column(String, nullable=False)  # VARCHAR
    benefits = Column(String, nullable=True)  # VARCHAR
    description = Column(String, nullable=True)  # VARCHAR
    employment_type = Column(String, nullable=True)  # VARCHAR
