#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
from models.base_model import Base
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review

from sqlalchemy.orm import sessionmaker


class DBStorage:
    """This class manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the db engine"""
        from sqlalchemy import (create_engine)
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    os.environ.get('HBNB_MYSQL_USER'),
                    os.environ.get('HBNB_MYSQL_PWD'),
                    os.environ.get('HBNB_MYSQL_HOST'),
                    os.environ.get('HBNB_MYSQL_DB')), pool_pre_ping=True)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = []
        if cls:
            objs.extend(self.__session.query(cls).all())
        else:
            for cls in [State, City]:
                objs.extend(self.__session.query(cls).all())

        return {obj.to_dict()['__class__'] + '.' + obj.id: obj
                for obj in objs}

    def new(self, obj):
        """Adds new object to the current database session"""
        self.__session.add(obj)
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current database session"""
        if not obj:
            return
        self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        """from models.user import User
        from models.place import Place"""
        from models.state import State
        from models.city import City
        """from models.amenity import Amenity
        from models.review import Review"""

        Base.metadata.create_all(self.__engine)
