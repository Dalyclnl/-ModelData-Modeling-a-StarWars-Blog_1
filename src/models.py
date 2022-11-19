import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(80),primary_key=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(80), nullable=False , unique=True)
    
   
class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    favoritos = relationship (User)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    characters = relationship (Favoritos)
   
 
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(80))
    planets = relationship (Favoritos)

 
def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


 
