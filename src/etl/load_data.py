# ----------------------------------------------------------------------
# File: src/load_data.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 26 jun 2021
# Brief: Load module for ETL services.
# ----------------------------------------------------------------------
import os

import psycopg2

import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from helpers.logging import logging, timed
from helpers.exceptions import GenericException


class LoadDataClass:
    """
    Load entire data to the DB.
    """

    def __init__(self, data_to_load: pd.DataFrame) -> None:
        """Constructor LoadClass method.

        Args:
            data_to_load (pd.Dataframe): Received Dataframe to load.
        """
        self.engine: Engine = create_engine(os.environ.get('DATABASE_URL'))
        self.conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
        self.conn.autocommit = True
        self.data_to_load: pd.DataFrame = data_to_load

    @timed
    def load(self) -> None:
        """Load main method

        Raises:
            DataAlreadyPersisted: Raises whether table already exists on the DB.
            GenericException: Raises whether an unexpected error appears.
        """
        try:
            # ------------------------------------
            # Create the purchase_table into the DB.
            self._create_staging_table(self.conn.cursor())

            # ------------------------------------
            # Persit columns and its data into the created ta table.
            self.data_to_load.to_sql(
                'purchase_data',
                self.engine,
                index=False,
                if_exists='append'
            )
            logging.info('Data has been persisted on the database.')

        except Exception as e:
            logging.error(f'Generic error. LOG: {e}')
            raise GenericException(e)

    @timed
    def _create_staging_table(self, cursor: object) -> None:
        """Create data table into DB according to the SQL script.

        Args:
            cursor (object): Cursor object from psycopg2
        """
        cursor.execute(open('src/sql_commands/create_table.sql', 'r').read())
