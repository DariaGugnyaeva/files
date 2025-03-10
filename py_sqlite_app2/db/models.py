from sqlalchemy import create_engine, ForeignKey, Table, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref, declarative_base
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


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
    id = Column(Integer, primary_key=True, nullable=False)
    relative_id = relationship(
                                'Project',
                                secondary=association_table,
                                backref='User'
                            )
    username = Column(String(40), nullable=False, unique=True)
    email = Column(String(40), nullable=False)

class Profile(Base):
    # имя, фамилия, отчество, номер читательского билета, адрес
    __tablename__ = "Profile"
    id = Column(Integer, primary_key=True)
    bio = Column(String(30), nullable=False)
    phone = Column(String(15), nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), unique=True, nullable=False)
    # person = relationship('User', backref='user_id', uselist=False)

class Project(Base):
    __tablename__ = "Project"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(40), nullable=False)
    description = Column(String(250), nullable=False)
    relative_id = relationship(
                                'User',
                                secondary=association_table,
                                backref='Project'
                            )

class Task(Base):
    __tablename__ = "Task"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(40), nullable=False)
    status = Column(Boolean)  # дефолтное никогда не используется
    project_id = Column(Integer, ForeignKey("Project.id"))
    project = relationship('Project', backref='Task')

engine = create_engine("sqlite:////Users/Вадим/OneDrive/Рабочий стол/py_sqlite_app2/library2.db")
Base.metadata.create_all(engine)
