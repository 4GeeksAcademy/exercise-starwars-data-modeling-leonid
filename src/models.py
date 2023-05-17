import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    dob = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    #film_id = Column(String(250), ForeignKey("films.id"))
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(float(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey("planets.id"))
    planet = relationship("Planets")

class Cast(Base):
    __tablename__ = 'cast'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, foreignKey("films.id"))
    film = relationship("Films", backref="cast")
    people_id = Column(Integer, ForeignKey("people.id"))
    people = relationship("People")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    weather = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(float(250), nullable=False)
    orbital_period = Column(float(250), nullable=False)




class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
