import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime  # Añadido DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    registration_date = Column(DateTime, nullable=False)  # Utilizando DateTime

    favorites = relationship("Favorite", back_populates="user")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(String(20), nullable=False)
    entity_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="favorites")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500))
    climate = Column(String(100))
    terrain = Column(String(100))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    species = Column(String(100))
    gender = Column(String(20))
    description = Column(String(500))

render_er(Base, 'diagram.png')
