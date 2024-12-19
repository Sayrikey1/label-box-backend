# db.py

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from .config import SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Dependency to get the metadata
def get_metadata():
    return metadata