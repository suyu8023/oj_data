import datetime
from dateutil.relativedelta import relativedelta


end_time = datetime.datetime.now()
print(end_time)
start_time = datetime.datetime.now() - relativedelta(months=+1)
print(start_time)
