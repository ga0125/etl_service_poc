# ----------------------------------------------------------------------
# File: src/extract_data.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 25 jun 2021
# Brief: Extract module for ETL services.
# ----------------------------------------------------------------------
import glob
import pandas as pd

from helpers.logging import logging
from helpers.constants import columns
from helpers.exceptions import FileNotFound


class ExtractDataClass:
    """
    Extract data from txt/csv file and load to in-memory dataframe.
    """

    def __init__(self) -> None:
        """Constructor ExtractDataClass method
        """
        self.files_to_process: list = glob.glob('data/*.txt')

    def _get_from_csv(self, file: list) -> pd.DataFrame:
        """Get txt/csf file and load to dataframe.

        Args:
            file (list): Extracted file.

        Returns:
            pd.DataFrame: Loaded dataframe.
        """
        return pd.read_csv(
            file,
            delim_whitespace=True,
            names=columns,
            skiprows=1
        )

    def extract(self) -> pd.DataFrame:
        """Extract main method.

        Raises:
            FileNotFound: Raises whether there's no file on data folder.

        Returns:
            pd.DataFrame: Loaded dataframe with extracted data.
        """

        extracted_data = pd.DataFrame()

        if not self.files_to_process:
            raise FileNotFound()

        for csvfile in self.files_to_process:
            extracted_data: pd.DataFrame = extracted_data.append(
                self._get_from_csv(csvfile), ignore_index=True)

        logging.info('Load data from CSV/txt to dataframe.')

        return extracted_data
