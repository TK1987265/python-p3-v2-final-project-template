

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()



engine = create_engine('sqlite:///wrestling.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


