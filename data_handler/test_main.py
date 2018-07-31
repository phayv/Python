from modules.phay_mods import *
from modules.library import *
import pytest


TEST_FILE = "data_sources/sf_restaurant_subset.csv"


@pytest.fixture(scope='module')
def data():
	return read_file(TEST_FILE)

def test_read_file(data):
	assert len(data) == 100
	assert len(data[0].keys()) == 17
	assert ('inspection_type' in data[0].keys())

def test_filter_inspection_type():
	data = [
		{'inspection_type' : 'A'},
		{'inspection_type' : 'B'},
		{'inspection_type' : 'C'},
		{'inspection_type' : 'A'}
	]

	assert filter_inspection_type(data, 'A') == [
		{'inspection_type' : 'A'}, {'inspection_type' : 'A'}]
	assert filter_inspection_type(data, 'B') == [
		{'inspection_type' : 'B'}]

	#edge case
	assert filter_inspection_type([], 'A') == []
	assert filter_inspection_type(data, 'Z') == []

def test_filter_month(data):
	assert len(filter_month(data, 5, 2017)) == 23
	assert len(filter_month(data, 12, 2017)) == 12
	assert filter_month(data, 12, 1400) == []

def test_count_risk_categories(data):
	assert count_risk_categories(data) == {
		'Low Risk' : 35,
		'Moderate Risk': 31,
		'High Risk' : 10,
		'No Violations' : 1,
		'' : 24,
	}

def test_risk_categories_by_month(data):
    result = count_risk_categories_by_month(data, 5, 2018)
    assert result == {'Low Risk': 35}