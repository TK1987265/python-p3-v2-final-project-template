from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    wrestlers = relationship("Wrestler", back_populates="team")

class Wrestler(Base):
    __tablename__ = 'wrestlers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    weight_class = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="wrestlers")

# Setup the database connection and session
engine = create_engine('sqlite:///wrestling.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
