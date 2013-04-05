from sqlalchemy import Column, Integer, String, Text

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class QueryBase(Base):
    @classmethod
    def query(cls):
        return DBSession.query(cls)


class MyModel(QueryBase):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Text)


class User(QueryBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(36))


class Pad(object):
    pass


class Note(object):
    pass
