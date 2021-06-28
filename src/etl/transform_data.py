# ----------------------------------------------------------------------
# File: src/transform_data.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 25 jun 2021
# Brief: Transform module for ETL services.
# ----------------------------------------------------------------------
import pandas as pd

from validate_docbr import CPF

from helpers.logging import logging
from helpers.constants import columns_to_filter
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
        self.cpf_handler = CPF()

    def _char_handler(self, columns: list, df: pd.DataFrame) -> pd.DataFrame:
        """Clear NaN characters from the received columns.

        Args:
            columns (list): Columns list to apply the regex.
            df (pd.DataFrame): Dataframe object.

        Returns:
            pd.DataFrame: [description]
        """
        df.loc[:, columns] = df.loc[:, columns].replace(
            to_replace=r'\D+',
            value='',
            regex=True
        )

        return df

    def transform(self) -> pd.DataFrame:
        """Transform main method

        Returns:
            pd.DataFrame: Filtered data.
        """
        try:
            # ------------------------------------
            # Remove NA/NaN values and duplicated lines from in-memory dataframe.
            filtered_data: pd.DataFrame = self.data.dropna()
            filtered_data.drop_duplicates()
            logging.info('Remove NA/NaN values and duplicated lines.')

            # ------------------------------------
            # Validate CPF column values and drop from Dataframe whether any CPF is invalid.
            for index, rows in filtered_data['cpf'].iteritems():
                if not self.cpf_handler.validate(rows):
                    filtered_data: pd.DataFrame = filtered_data.drop(
                        index, axis=0)

            logging.info('Validate CPF column values.')

            # ------------------------------------
            # Remove some "dirts" chars of the CPF and CNPJ from the dataset.
            # columns_to_filer: list = Received from helpers.constants.py
            filtered_data = self._char_handler(
                columns_to_filter, filtered_data)

            logging.info('Remove unused characters from doc values.')

            return filtered_data

        except Exception as e:
            logging.error(f'Generic error. LOG: {e}')
            raise GenericException(e)
