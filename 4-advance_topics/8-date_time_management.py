"""
    Important Points::
    => http://strftime.org/  (Refer this url for date and time formatting patterns)
"""

import datetime
from datetime import timedelta


if __name__ == '__main__':
    # get current date and time
    current_date_and_time = datetime.datetime.now()  # datetime object
    print(current_date_and_time)

    current_date = current_date_and_time.date()  # datetime.date object
    print(current_date)

    current_time = current_date_and_time.time()  # datetime.time object
    print(current_time)

    # get custome datetime object
    custom_datetime = datetime.datetime(2015, 10, 27)
    print(custom_datetime) # 2015-10-27 00:00:00

    # add time into datetime object
    customized_time = custom_datetime + timedelta(hours=2, minutes=15, seconds=20)
    print(customized_time)  # 2015-10-27 02:15:20

    # change formatting of date and time
    format1 = current_date_and_time.strftime('%Y-%m-%d %H:%M:%S')  # str object
    print('format1 =>', format1)  # 2019-07-31 18:21:38

    format2 = current_date_and_time.strftime('%b %d %Y')  # str object
    print('format2 =>', format2)  # Jul 31 2019
