"""
    Various helper funcs
"""


import datetime


def log_msg(log_string):
    timestamp = str(datetime.datetime.now())[:-7]
    print(f'{timestamp}  |  {log_string}')
