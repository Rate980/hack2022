from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

host = "mysql_db"
db_name = "employees"
user = "user"
password = "password"

DATABASE = f"mysql://{user}:{password}@{host}/{db_name}?charset=utf8"
ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=ENGINE))

Base = declarative_base()
Base.query = session.query_property()
