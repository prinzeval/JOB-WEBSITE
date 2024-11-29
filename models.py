from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JobListing(Base):
    __tablename__ = 'Job_listing'

    "id" = Column(Integer, primary_key=True, autoincrement=True)
    "POSITION" = Column(String, nullable=False)  # VARCHAR
    "COMPANY NAME" = Column(String, nullable=False)  # VARCHAR
    "LOCATION" = Column(String, nullable=False)  # VARCHAR
    "SALARY" = Column(String, nullable=True)  # VARCHAR
    "JOB LINK" = Column(String, nullable=False)  # VARCHAR
    "BENEFITS" = Column(String, nullable=True)  # VARCHAR
    "DESCRIPTION" = Column(String, nullable=True)  # VARCHAR
    "EMPLOYMENT TYPE" = Column(String, nullable=True)  # VARCHAR
