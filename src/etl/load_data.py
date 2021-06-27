# ----------------------------------------------------------------------
# File: src/load_data.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 26 jun 2021
# Brief: Load module for ETL services.
# ----------------------------------------------------------------------
import os
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from helpers.logging import logging
from helpers.exceptions import (
    GenericException,
    DataAlreadyPersisted
)


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
        self.data_to_load: pd.DataFrame = data_to_load

    def load(self) -> None:
        """Load main method

        Raises:
            DataAlreadyPersisted: Raises whether table already exists on the DB.
            GenericException: Raises whether an unexpected error appears.
        """
        try:
            # ------------------------------------
            # Persit columns and its data to the DB.
            self.data_to_load.to_sql(
                'purchase_data',
                self.engine,
                index=False
            )
            logging.info('Data has been persisted on the database.')

        # ------------------------------------
        # Verify whether the table is already created and raises an exception if necessary.
        except ValueError as e:
            if 'already exists' in str(e):
                logging.error('Table already exists.')
                raise DataAlreadyPersisted()

            raise GenericException(e)

        except Exception as e:
            logging.error(f'Generic error. LOG: {e}')
            raise GenericException(e)
