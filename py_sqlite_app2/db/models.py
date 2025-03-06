from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from db import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)

class Profile(Base):
    # имя, фамилия, отчество, номер читательского билета, адрес
    __tablename__ = "Profile"
    id = Column(Integer, primary_key=True)
    bio = Column(String(30), nullable=False)
    phone = Column(String(15), nullable=False)
    user_id = Column(Integer, nullable=False, unique=True, ForeignKey("User.id"))

class Project(Base):
    __tablename__ = "Project"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(40), nullable=False)
    description = Column(String(250), nullable=False)

class Task(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(40), nullable=False)
    status = Column(Boolean, default=False)
    project_id = Column(Integer, nullable=False, unique=True, ForeignKey("Project.id"))

Base.metadata.create_all(engine)
