# ----------------------------------------------------------------------
# File: src/transform_data.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 25 jun 2021
# Brief: Transform module for ETL services.
# ----------------------------------------------------------------------
import pandas as pd

from helpers.logging import logging
from helpers.validators import CPFValidator
from helpers.exceptions import GenericException


class TransformDataClass:
    """
    Transform and validate data before to persist on the DB.
    """

    def __init__(self, data: pd.DataFrame) -> None:
        """constructor method

        Args:
            data (pd.DataFrame): Extracted data
        """
        self.data: pd.DataFrame = data

    def transform(self) -> pd.DataFrame:
        """Transform main method

        Returns:
            pd.DataFrame: Filtered data.
        """

        try:
            # ------------------------------------
            # Remove NA/NaN values and duplicated lines from in-memory dataframe.
            filtered_data = self.data.dropna()
            filtered_data.drop_duplicates()
            logging.info('Remove NA/NaN values and duplicated lines.')

            # ------------------------------------
            # Validate CPF column values and drop from Dataframe whether any CPF is invalid.
            for index, rows in filtered_data['cpf'].iteritems():
                if not CPFValidator(rows).validate():
                    filtered_data = filtered_data.drop(index, axis=0)

            logging.info('Validate CPF column values.')
            return filtered_data

        except Exception as e:
            logging.error(f'Generic error. LOG: {e}')
            raise GenericException(e)
