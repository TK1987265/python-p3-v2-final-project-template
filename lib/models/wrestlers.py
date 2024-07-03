# Example: wrestler.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base  # Import Base from base module

class Wrestler(Base):
    __tablename__ = 'wrestlers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight_class = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates="wrestlers")
