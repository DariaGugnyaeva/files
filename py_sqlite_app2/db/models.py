from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from db import engine

Base = declarative_base()

association_table = Table(
                       'association', Base.metadata,
                       Column('user_id', Integer, ForeignKey('User.id')),
                       Column('project_id', Integer, ForeignKey('Project.id'))
                      )
# добавить функцию с назначением пользователя на проект
# id добавлять ручками
class User(Base):
    __tablename__ = "User"
    id = relationship('Project', secondary=association_table, back_populates='User')
    username = Column(String(40), nullable=False, unique=True)
    email = Column(String(40), nullable=False)

class Profile(Base):
    # имя, фамилия, отчество, номер читательского билета, адрес
    __tablename__ = "Profile"
    id = Column(Integer, primary_key=True)
    bio = Column(String(30), nullable=False)
    phone = Column(String(15), nullable=False)
    user_id = Column(Integer, nullable=False, ForeignKey("User.id"), unique=True)
    person = relationship('User', backref='user_id', uselist=False)

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
