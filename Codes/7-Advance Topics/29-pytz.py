"""
    Important Points::
    => It is recommended that datetime handling should be done using UTC timezone
"""
import pytz
from dateutil import tz
from datetime import datetime


if __name__ == '__main__':
    # setting timezones
    utc_timezone = pytz.utc
    print('utc_timezone::', utc_timezone.zone)

    eastern_timezone = pytz.timezone('US/Eastern')
    print('eastern_timezone::', eastern_timezone.zone)

    pakistan_timezone = pytz.timezone('Asia/Karachi')
    print('pakistan_timezone::', pakistan_timezone.zone)

    # getting current time of different time zones
    dubai_datetime_obj = datetime.now(pytz.timezone('Asia/Dubai'))
    dubai_datetime = dubai_datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    print('Dubai date & time::', dubai_datetime)

    # getting utc time of particular timezone
    utc_datetime_obj = datetime.utcnow()
    pak_datetime_obj = utc_datetime_obj.astimezone(pakistan_timezone)
    pak_datetime = pak_datetime_obj.strftime('%Y-%m-%d %H:%M:%S %Z%z')
    print('Pakistan utc date & time::', pak_datetime)

    # getting datetime of a timezone by using its utc time
    eastern_datetime_obj = datetime.now(tz.gettz('UTC-5'))
    eastern_datetime = eastern_datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    print('Eastern date & time::', eastern_datetime)

    # getting datetime of a timezone
    prague_datetime_obj = datetime.now(pytz.timezone('Europe/Prague'))
    prague_datetime = prague_datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
    print('Prague date & time::', prague_datetime)
