from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from datetime import datetime
import os

# project directory path
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# connection string for db
connection_string = "sqlite:///"+os.path.join(BASE_DIR,'site.db')


Base = declarative_base()
engine = create_engine(connection_string, echo=True)
Session = sessionmaker()

"""
class User
    id int
    username str
    email str
    date_created datetime
"""

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True )
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


new_user = User(id=1, username='johar', email='johar@gmail.com')
print(new_user)
