from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./trustscan.db"


engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


# Utilitário de dependência
class ExampleModel(Base):
	__tablename__ = 'example'
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True)
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()