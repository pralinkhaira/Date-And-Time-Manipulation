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
from DateTimeUtils import DateTimeUtils

# Parse a date string
date_str = "2023-05-05"
date_obj = DateTimeUtils.parse_date(date_str)

# Format a date object
formatted_date_str = DateTimeUtils.format_date(date_obj)

# Add days to a date object
new_date_obj = DateTimeUtils.add_days(date_obj, 7)

# Subtract days from a date object
new_date_obj = DateTimeUtils.subtract_days(date_obj, 3)

# Convert timezone of a date object
new_date_obj = DateTimeUtils.convert_timezone(date_obj, from_timezone=0, to_timezone=-5)
```

## Contributing

If you'd like to contribute to the library, please open an issue or submit a pull request. We welcome all contributions, including bug fixes, new features, and documentation improvements.

## License

This library is licensed under the [GNU License](LICENSE.txt).
