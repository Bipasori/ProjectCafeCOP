# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

user_name = "..."
user_pwd = "..."
db_host = "..."
db_name = "..."

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    user_pwd,
    db_host,
    db_name,
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()