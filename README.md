![](logo.png)

### What does it do?
Have you ever had a time when your missing data was holding you back? Well then this package is for you!

Our python package for simple data imputation will allow you to quickly and seamlessly impute any missing data (be numeric, categorical, date/time or boolean values) using any large datasets.

All you have to do is follow these simple 4 steps:
 1. Import the package and the data you wish you impute
 2. Select the function and method for imputation (this will depend on the data type - read the usage section below for more details)
 3. Hit run
 4. Save your newly imputed dataset

Our package will help simplify all your imputation needs so your data is ready when you need it!

## Contributors & Maintainers
- [Lisa Sequeira](https://github.com/LisaSeq)
- [Renee Kwon](https://github.com/renee-kwon)
- [Fujie Sun](https://github.com/Althrun-sun)
- [Ken Wang](https://github.com/kenuiuc)

## Installation

```bash
$ pip install simpute_py
```

## Usage and Examples

We have four main functions dealing with each data type:
- `Num_imputer`: This function fills in the empty values of a numeric column with values derived from your selected imputation method. Your options for method include _knn_ (autogenerated values based on KNN), _mean_, _median_ and _mode_.
- `Cat_imputer`: This function fills in the empty values of a categorical column with values derived based on most frequent (mode) category.
- `Bol_imputer`: This function fills in the empty values of a boolean column with values derived using most frequent (mode) boolean value.
- `Date_imputer`: This function fills in empty values of a date column with median point of the range of dates in that column.

To get started first install our imputation functions:

```ruby
from simpute_py.bol_imputer import bol_imputer #For imputing on boolean columns
from simpute_py.cat_imputer import cat_imputer #For imputing on categorical columns
from simpute_py.date_imputer import date_imputer #For imputing on date columns
from simpute_py.num_imputer import num_imputer #For imputing on numerical columns
```

To run to the function, simply enter the following:

``` ruby
import pandas as pd

#Load test data from home directory
test_df = pd.read_csv('tests/tesla_deaths_mini.csv')

#Test functions
test_df = bol_imputer(test_df, "Driver")
test_df = cat_imputer(test_df, "Country")
test_df = date_imputer(test_df, "Date")
test_df = num_imputer(test_df, "Deaths")

print(test_df)
```

## Place in the Python Ecosystem

Currently, there are many other ways you can impute a dataset, using various functions build within Python, but this packages it neatly into one place and simplifies the process. We do have other packages you can use such as [AutoImpute](https://pypi.org/project/autoimpute/) and [MIDASpy](https://github.com/MIDASverse/MIDASpy). However our package aims to provide functionality not provided in either package and for more general audience use.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`simpute_py` was created by Lisa Sequeira, Renee Kwon, Fujie Sun, and Ken Wang. It is licensed under the terms of the MIT license.

## Credits

`simpute_py` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

