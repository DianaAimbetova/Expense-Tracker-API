import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import settings


DATABASE_URL = settings.database_url

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
Base = declarative_base(metadata=metadata)
