from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    client_name = Column(String)
    country = Column(String)

class Vessel(Base):
    __tablename__ = 'vessel'
    id = Column(Integer, primary_key=True)
    vessel_name = Column(String)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", backref="vessels")

class Berthing(Base):
    __tablename__ = 'berthing'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    start_time = Column(DateTime)
    end_date = Column(DateTime)
    end_time = Column(DateTime)
    days_in_port = Column(Integer, default=0)
    vessel_id = Column(Integer, ForeignKey('vessel.id'))
    vessel = relationship("Vessel", backref="berthings")

# Create the database engine
engine = create_engine('sqlite:///database.db')

# Create the tables in the database
Base.metadata.create_all(engine)
