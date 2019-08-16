import pandas as pd
import numpy as np

a = pd.Series([1, 3, 5, np.nan, 10])

date = pd.date_range('20190106', periods=6)


df = pd.DataFrame(np.random.randn(6,4), index=date, columns=list('ABCD'))

print(df)

# import datetime
# import jdatetime
# import calendar
#
# print(calendar.monthcalendar(2019, 10))
#
# print(datetime.datetime.now())
# print(jdatetime.datetime.now())