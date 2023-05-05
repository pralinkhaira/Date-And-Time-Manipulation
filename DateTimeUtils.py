import datetime

class DateTimeUtils:
    @staticmethod
    def parse_date(date_str, format_str="%Y-%m-%d"):
        return datetime.datetime.strptime(date_str, format_str).date()

    @staticmethod
    def format_date(date_obj, format_str="%Y-%m-%d"):
        return date_obj.strftime(format_str)

    @staticmethod
    def add_days(date_obj, days):
        return date_obj + datetime.timedelta(days=days)

    @staticmethod
    def subtract_days(date_obj, days):
        return date_obj - datetime.timedelta(days=days)

    @staticmethod
    def convert_timezone(date_obj, from_timezone, to_timezone):
        from_tz = datetime.timezone(datetime.timedelta(hours=from_timezone))
        to_tz = datetime.timezone(datetime.timedelta(hours=to_timezone))
        return date_obj.replace(tzinfo=from_tz).astimezone(to_tz)

