# ----------------------------------------------------------------------
# File: src/main.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 23 jun 2021
# Brief: Main module for ETL services.
# ----------------------------------------------------------------------
from etl.extract_data import ExtractDataClass
from etl.transform_data import TransformDataClass
from etl.load_data import LoadDataClass


extracted_data = ExtractDataClass().extract()
tranformed_data = TransformDataClass(extracted_data).transform()
load_data = LoadDataClass(tranformed_data).load()
