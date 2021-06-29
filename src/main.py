# ----------------------------------------------------------------------
# File: src/main.py
# Author: Gabriel Zacchi Braga (Owner)
# Date: 23 jun 2021
# Brief: Main module for ETL services.
# ----------------------------------------------------------------------
from etl.extract_data import ExtractDataClass
from etl.transform_data import TransformDataClass
from etl.load_data import LoadDataClass


# -----------------------------
# Initialize and extract data from data folder
extracted_data = ExtractDataClass().extract()

# -----------------------------
# Initialize and tranform data, filtering the DataFrame
tranformed_data = TransformDataClass(extracted_data).transform()

# -----------------------------
# Initialize and load data into the database
load_data = LoadDataClass(tranformed_data).load()
