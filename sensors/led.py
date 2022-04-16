import time
import datetime

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def LedOn(timer):
    return 'true'
def LedOff():
    return 'false'
