# Date and Time Manipulation Library

This library provides a set of utility functions for working with dates and times in Python. It is designed to simplify common tasks such as parsing and formatting dates, performing date arithmetic, and converting time zones.

## Installation

You can clone the repository and install it. To do so, run the following commands:

```bash
git clone https://github.com/BitH0xker/Date-And-Time-Manipulation.git
cd Date-And-Time-Manipulation
```

## Usage

To use the library, simply import the `DateTimeUtils` class and call its methods as necessary. Here's an example:

```python

# Parsing dates
date_str = "2022-12-31"
date_obj = DateTimeUtils.parse_date(date_str)

# Formatting dates
date_str = DateTimeUtils.format_date(date_obj)

# Adding and subtracting days
new_date_obj = DateTimeUtils.add_days(date_obj, 7)
newer_date_obj = DateTimeUtils.subtract_days(date_obj, 7)

# Calculating the difference between two dates
days_diff = DateTimeUtils.difference_in_days(date_obj, new_date_obj)

# Finding the last day of a month
last_day = DateTimeUtils.last_day_of_month(date_obj)

# Determining whether a year is a leap year
is_leap_year = DateTimeUtils.is_leap_year(2022)

# Converting time zones
new_date_obj = DateTimeUtils.convert_timezone(date_obj, "UTC", "US/Pacific")

# Getting a list of available time zones
timezones = DateTimeUtils.get_available_timezones()

```

## Update Info

**Initial commit**

This commit includes the initial version of the DateTimeUtils library. It provides a set of utility methods for date and time manipulation, including parsing dates, formatting dates, adding and subtracting days, calculating the difference between two dates, finding the last day of a month, and converting time zones.

**Version 1.1**

This version of the DateTimeUtils library includes the following changes:

- Added a new method `get_day_of_week` to return the day of the week of a given date.
- Refactored the code to improve readability and maintainability.
- Updated the README.md file to include more detailed instructions and examples.

## Supported Formats

The `parse_date` and `format_date` methods support any valid date format string that can be used with `datetime.datetime.strptime` and `strftime`.

## Time Zones

The `convert_timezone` method uses the `pytz` library to support time zone conversions between any two time zones. The method raises a `ValueError` if either the `from_timezone` or `to_timezone` parameter is not a valid time zone identifier.

The `get_available_timezones` method returns a list of all available time zones.


## Contributing

If you'd like to contribute to the library, please open an issue or submit a pull request. We welcome all contributions, including bug fixes, new features, and documentation improvements.

## License

This library is licensed under the [GNU License](LICENSE.txt).
