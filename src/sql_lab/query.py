#!/usr/bin/env python3

'''Create two functions, one that returns the count of a particularly selected value in a column, and another that returns a barchart of counts of the values of a column'''

import logging
import os
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

DBHOST = os.environ.get("DBHOST")
DBUSER = os.environ.get("DBUSER")
DBPASS = os.environ.get("DBPASS")
DBNAME = os.environ.get("DBNAME")

TABLE = "mock"

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DBNAME)
cur = db.cursor()

def get_data_by_group(value):
	'''takes in a string value which we use to select a particular group in our mock data to count'''
	query = f"SELECT * FROM {TABLE} WHERE group_name = %s;"
	try:
		cur.execute(query,(value,))
		results = cur.fetchall()
		output = []
		for r in results:
			output.append(r)
		return output
	except mysql.connector.Error as e:
		print("MySQL Error: ", str(e))
		return None

def plot_counts(groupby):
	'''counts rows by distinct value per column selected, and outputs a bar chart'''
	query = f"SELECT `{groupby}`, COUNT(*) FROM {TABLE} GROUP BY `{groupby}`;"
	try:
		cur.execute(query)
		results = cur.fetchall()
		output = []
		for r in results:
			output.append(r)
		df = pd.DataFrame(output)
		df.plot.bar(x=0, y=1)
		plt.tight_layout()
		plt.show()
		return df
	except mysql.connector.Error as e:
		print("MySQL Error: ", str(e))
		return None

def main():
	'''run the previous two functions, and close the database connection'''
	print('Output # of row by group name:')
	print(get_data_by_group("video"))
	print('Output plot of counts by group name:')
	plot_counts("group_name")
	cur.close()
	db.close()
if __name__ == "__main__":
        main()
	
