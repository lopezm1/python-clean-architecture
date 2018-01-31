from abc import ABC
from sqlalchemy import create_engine, MetaData
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class BaseMySQL(ABC): #ABC decorator needed for children objects to follow ABC instantiation rules
    def __init__(self):
        self.conn_str = 'mysql+pymysql://{username}:{password}@{db_connection}/{db_name}?charset=utf8'
        """
        Comment out DB Engine for now.
        self.engine = create_engine(
            self.conn_str.format(
                username=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD'],
                db_connection=os.environ['DB_CONNECTION'],
                db_name=os.environ['DB_NAME']
            ),
            pool_recycle=3600
        )
        self.metadata = MetaData()
        """








