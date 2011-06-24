# -*- coding: utf-8 -*-
#
# Author: Steven Christe <steven.d.christe@nasa.gov>
#
# <License info will go here...>
"""Provides utility programs.

    Notes: 
    The astronomy-type utilities should probably be separated out into
    another file. 
    --schriste

"""

import datetime
import numpy as np


def anytim(time_string = None):
    """Given a time string will parse and return a datetime object.
    If no string is given then returns the datetime object for the current time.
    (Right now this function does nothing but return the current datetime object).
    """
    if time_string is None:
        time = datetime.datetime.now()
    else:
        # Expects the following input
        # 2011/04/04 00:00:00
        # TODO: add code to parse more time string!
        year = int(time_string[0:4])
        month = int(time_string[5:7])
        day = int(time_string[8:10])
        if len(time_string) >= 11:
            hour = int(time_string[11:13])
            minute = int(time_string[14:16])
        else:
            hour = minute = 0
        if len(time_string) >= 20:
            second = int(time_string[17:19])
        else:
            second = 0
        if len(time_string) == 23:
            millisecond = int(time_string[20:24])
            microsecond = 1000*millisecond
        else:
            microsecond = millisecond = 0
        time = datetime.datetime(year,month,day,hour,minute,second,microsecond)
    return time

def julian_day(t=None):
    """Returns the (fractional) Julian day."""
    # The number of days between Jan 1 1900 and the Julian
    # reference date of 12:00 noon Jan 1, 4713 BC
    JULIAN_DAY_ON_NOON01JAN1900 = 2415020.5
    DAYS_IN_YEAR = 36525.0
    SECONDS_IN_DAY = 60*60*24.0
    jul = anytim(t) - datetime.datetime(1900, 1, 1, 0, 0, 0)
    result = jul.days + jul.seconds/SECONDS_IN_DAY
    return result + JULIAN_DAY_ON_NOON01JAN1900

def julian_centuries(t=None):
    """Returns the number of Julian centuries since 1900 January 0.5"""
    # The number of days between Jan 1 1900 and the Julian
    # reference date of 12:00 noon Jan 1, 4713 BC
    JULIAN_DAY_ON_NOON01JAN1900 = 2415020.5
    DAYS_IN_YEAR = 36525.0
    result = (julian_day(t) - JULIAN_DAY_ON_NOON01JAN1900) / DAYS_IN_YEAR
    return result

def day_of_year(t=None):
    """Returns the day of year."""
    time = anytim(t)
    year = time.year
    time_diff = anytim(t) - datetime.datetime(time.year, 1, 1, 0, 0, 0)
    result = time_diff.days
    return result

def degrees_to_hours(angle):
    """Convert an angle from the degree notation to the hour, arcmin, arcsec 
    notation (return as a tuple)."""
    hour = int(np.floor(angle / 15))
    remainder = angle / 15.0 - hour
    print(remainder)
    arcminute = int(np.floor(remainder * 60))
    remainder =  remainder*60 - arcminute
    print(remainder)
    arcsecond = remainder * 60.0
    remainder = remainder * 60.0 - arcsecond
    print(remainder)
    print(hour*15 + arcminute/60.0 + arcsecond/(60*60.0))
    return [hour, arcminute, arcsecond]

