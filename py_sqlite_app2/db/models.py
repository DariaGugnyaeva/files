from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from db import engine

Base = declarative_base()

class Books(Base):
    __tablename__ = "Books"
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    author = Column(String(40), nullable=False)
    year = Column(Integer, nullable=False, unique=False, default=2025)
    edition = Column(Integer, nullable=False)
    num_bookcase = Column(Integer, nullable=False)
    num_shell = Column(Integer, nullable=False)

class Visitors(Base):
    # имя, фамилия, отчество, номер читательского билета, адрес
    __tablename__ = "Visitors"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(30), nullable=False)
    patr_name = Column(String(30), nullable=False, default="-")
    library_card = Column(Integer, unique=True)
    address = Column(String(50), nullable=False)

class Readers(Base):
    __tablename__ = "Readers"
    id = Column(Integer, primary_key=True, nullable=False)
    id_vis = Column(Integer, ForeignKey("Visitors.id"), nullable=False)
    id_book = Column(Integer, ForeignKey("Books.id"), nullable=False)

Base.metadata.create_all(engine)
