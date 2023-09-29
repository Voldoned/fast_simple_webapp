from sqlalchemy import NullPool, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

# Create a sqlite engine instance
URL_DB = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(URL_DB, pool_pre_ping=True, poolclass=NullPool, pool_recycle=3600)

# Create a DeclarativeMeta instance
Base = declarative_base()

metadata = MetaData()


session_maker = sessionmaker(
    bind=engine,
    class_=Session,
    expire_on_commit=False,
)

def init_db():
    Base.metadata.create_all(bind=engine)


def get_session():
    with session_maker() as session:
        yield session
        # session.close()
