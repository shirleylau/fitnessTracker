import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('mysql://root:pa55word@localhost:3306/fitnessDB')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key = True)
    first_name = Column(String(25), nullable = False)
    last_name = Column(String(25))
    username = Column(String(25), unique = True, nullable = False)
    password = Column(String(25), nullable = False)
    # workouts = relationship('Workout')


class Workout(Base):
    __tablename__ = 'workout'
    id = Column(BigInteger, primary_key = True)
    name = Column(String(25), nullable = False)
    operation = Column(String(25), nullable = False)


class User_Workout_History(Base):
    __tablename__ = 'user_workout_history'
    user_id = Column(ForeignKey('user.id'), primary_key = True)
    date = Column(DateTime, primary_key = True, default = datetime.now, nullable = False)
    workout_id = Column(ForeignKey('workout.id'), primary_key = True)
    reps = Column(Integer, nullable = False)


class User_Bodyweight_History(Base):
    __tablename__ = 'user_bodyweight_history'
    user_id = Column(ForeignKey('user.id'), primary_key = True)
    # user = relationship('User')
    date = Column(DateTime, primary_key = True, default = datetime.now, nullable = False)
    bodyweight = Column(Integer, nullable = False)


session = db_session()


def find_user_by_username(username):
    return session.query(User).filter(User.username == username).one()


def find_user_by_id(id):    
    return session.query(User).filter(User.id == id).one()


def create_user(first_name, last_name, username, password):
    new_user = User(first_name=first_name, last_name=last_name, username=username, password=password)
    session.add(new_user)
    session.commit()


def delete_user(username):
    user = get_user(username)
    session.delete(user)
    session.commit()


def init():
    print('creating all db tables')
    Base.metadata.create_all(bind=engine)
