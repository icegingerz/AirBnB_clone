#!/usr/bin/python3
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """Database Storage for Airbnb"""
    __engine = None
    __session = None

    def __init__(self):
        """Create database engine with environment variables"""

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB'),
                pool_pre_ping=True))

        if getenv('HBNB_ENV') == 'test':
            # Drop all the tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects
        depending of the class name
        if cls=None:
             query all types of objects (User, State, City,
             Amenity, Place and Review)
        Returns:
            a dictionary: key = <class-name>.<object-id>
        """
        dict = {}
        if cls and type(cls) == 'str':
            cls = eval(cls)
            query = self.__session.query(cls)
            for q in query:
                key = type(q).__name__ + '.' + q.id
                dict[key] = q
        else:
            classes = [State, City]
            for cls in classes:
                query = self.__session.query(cls)
                for q in query:
                    key = type(q).__name__ + '.' + q.id
                    dict[key] = q
            # return {'{}.{}'.format(type(q).__name__, q.id): q for q in query}
        return dict

    def new(self, obj):
        """Add new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all table in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
