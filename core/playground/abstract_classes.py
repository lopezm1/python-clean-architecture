from abc import ABC, abstractmethod
from sqlalchemy import *
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BaseMySQL(ABC): #ABC decorator needed for children objects to follow ABC instantiation rules
    def __init__(self):
        self.conn_str = 'mysql+pymysql://{username}:{password}@{db_connection}/{db_name}?charset=utf8'
        self.metadata = MetaData()

class AddressInterface(BaseMySQL):


    @abstractmethod
    def get_address(self, value):
        pass

    @abstractmethod
    def insert_address_coords(self):
        pass

class AddressGeocodeQueueInterface(BaseMySQL):

    @abstractmethod
    def delete_address_id(self):
        self.lol = "hello from abstract"
        print("print during super")






