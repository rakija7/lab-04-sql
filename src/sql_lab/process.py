#!/usr/bin/env python3

import pandas as pd
import logging
from sqlalchemy import create_engine, text
import os
import mysql.connector

DBHOST = os.environ.get('DBHOST')
DBUSER = os.environ.get('DBUSER')
DBPASS = os.environ.get('DBPASS')
DBNAME = os.environ.get('DBNAME')

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

type_mapping = {
    "int64": "BIGINT",
    "int32": "INT",
    "float64": "DOUBLE",
    "bool": "TINYINT(1)",
    "datetime64[ns]": "DATETIME",
    "object": "VARCHAR(255)",  # safe default varchar length
    "string": "VARCHAR(255)",
}

def read_data(filename):
	'''loads in a CSV and turns it into a pandas dataframe'''
	logger.info("Reading data from %s",filename)
	data = pd.read_csv(filename)
	return data

def clean_data(data):
	'''cleans the dataframe by removing rows with missing columns and renaming columns, and casts types'''
	cleaned = data.copy()
	cleaned = cleaned.dropna()
	cleaned.columns = [col.strip().lower() for col in cleaned.columns]
	if "group" in cleaned.columns:
		cleaned = cleaned.rename(columns={"group": "group_name"})
	for col in cleaned.columns:
		if cleaned[col].dtype == "float64" and (cleaned[col] % 1 == 0).all():
			cleaned[col] = cleaned[col].astype("int64")
	logger.info("Cleaned data: %d rows remain", len(cleaned))
	return cleaned

def load_data(data, table):
	'''translate the dataframe to a MySQL table'''
	connection_url = (f"mysql+mysqlconnector://{DBUSER}:{DBPASS}@{DBHOST}:3306/{DBNAME}")
	engine = None
	try:
		engine = create_engine(connection_url)
		data.to_sql(table, con=engine, if_exists="append", index=False)
		logger.info("Loaded %d rows into '%s'", len(data), table)
	except Exception as e:
		logger.error("Upload failed: %s", str(e))
		raise
	finally:
		engine.dispose()

def main():
	'''run the extraction, transformation, and loading of the csv to an SQL table'''
	TABLE = 'mock'
	CSV_FILE = 'MOCK_DATA.csv'
	raw_data = read_data(CSV_FILE)
	cleaned_data = clean_data(raw_data)
	load_data(cleaned_data, TABLE)
	logger.info("Successful loading")

if __name__ == "__main__":
    main()
