import pandas as pd
import uuid
import random
from faker import Faker
from datetime import datetime
from datetime import timedelta

# def randomtimes(start, end):
#     frmt = "%Y-%m-%d %H:%M:%S"
#     stime = datetime.datetime.strptime(start, frmt)  
#     etime = datetime.datetime.strptime(end, frmt)
#     stime = start.total_seconds()
#     etime = end.total_seconds()

#     td = etime - stime

#     return td

frmt = "%Y-%m-%d %H:%M:%S"
mytime = "2023-02-15 00:00:00"
epoch = datetime(1970,1,1)
print((datetime.strptime(mytime, frmt)-epoch).total_seconds())

# # Setting the start and end times
# start = "2022-12-01 00:00:00"
# end = "2023-02-15 00:00:00"

