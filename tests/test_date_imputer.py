from simpute_py.date_imputer import date_imputer
import pytest

def test_date_imputer():
    output = date_imputer(0,0)
    assert output == "hello"
