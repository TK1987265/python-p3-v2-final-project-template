# # base.py or wherever your SQLAlchemy base and engine are defined
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()
# engine = create_engine('sqlite:///wrestling.db', echo=True)  # echo=True can help debug
# Session = sessionmaker(bind=engine)

# def init_db():
#     Base.metadata.create_all(engine)

# if __name__ == '__main__':
#     init_db()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)

# class Wrestler(Base):
#     __tablename__ = 'wrestlers'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     weight_class = Column(String)
#     team_id = Column(Integer, ForeignKey('teams.id'))
#     team = relationship("Team", back_populates="wrestlers")



# class Team(Base):
#     __tablename__ = 'teams'
#     id = Column(Integer, primary_key=True)
#     name = Column(String, unique=True)
#     wrestlers = relationship("Wrestler", back_populates="team")    


engine = create_engine('sqlite:///wrestling.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Using the ORM to insert and query data
# session = Session()
# new_user = User(name="John Doe")
# session.add(new_user)
# session.commit()

# users = session.query(User).all()
# for user in users:
#     print(user.name)
# session.close()
