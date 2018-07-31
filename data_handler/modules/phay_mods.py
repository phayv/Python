"""
Utilities for working with SF restaurant data.

"""
import csv
from collections import Counter


def read_file(filename):
	"""
	Read a CSV file of San Francisco public city restaurant inspection data.
	--https://data.sfgov.org/Health-and-Social-Services/Restaurant-Scores-LIVES-Standard/pyih-qa8i
	

	Returns list of dictionaries with one dictionary per row of the file.
	"""
	with open(filename) as file:
		reader = csv.DictReader(file)
		return list(reader)


def filter_inspection_type(data, inspection_type):
	"""
	Filter data to only include rows with a given inspection type
	"""
	return [row for row in data if row['inspection_type'] == inspection_type]


def filter_month(data, month, year):
	"""
	Filter data to only include rows from a given month.

	could use an API...
	EX: 05/07/2018 12:00:00 AM
	so we want month and year extracted...

	Returns a list of filtered data.
	"""
	input_month = str(month).zfill(2)
	input_year = str(year)

	month_data = []

	for row in data:
		date_as_string = row['inspection_date'][:10]
		month, day, year = date_as_string.split('/')
		if (input_month == month and input_year == year):
			month_data.append(row)

	return month_data


def count_risk_categories(data):
	"""
	Count the number of each risk category in a given dataset.

	Returns dictionary pairing a risk caetegory with a number of occurences.
	"""
	results = Counter([row['risk_category'] for row in data])
	if '' in results:
		results['No Violations'] = results['']
		del results['']
	return results

def count_risk_categories_by_month(data, month, year):
	"""
	Count the number of risk categories in a given month.

	"""
	return count_risk_categories(
		filter_inspection_type(
			filter_month(data, month, year), 'Routine - Unscheduled'))
