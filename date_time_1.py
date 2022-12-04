import datetime

# O'zgarmaslar.
# print("MAXYEAR: ", datetime.MAXYEAR)
# print("MINYEAR: ", datetime.MINYEAR)
# print("UTC: ", datetime.UTC)

date_1 = datetime.date(2022, 12, 2)
# print(date_1)
# print(date_1.day)
# print(date_1.month)
# print(date_1.year)

date_8 = datetime.time(21, 10, 1, 1)
# print(date_8.hour)
# print(date_8.minute)
# print(date_8.second)
# print(date_8.microsecond)

date_2 = datetime.datetime(2022, 12, 2, 21, 10, 1, 1)
date_3 = datetime.datetime.now()
date_4 = datetime.datetime.today()
print(date_3)
print(date_3.weekday())
# print(date_4)
# print(date_2)  # 2022-12-02 21:10:01.000001
# print(date_2.year)
# print(date_2.month)
# print(date_2.day)
# print(date_2.hour)
# print(date_2.minute)
# print(date_2.second)
# print(date_2.now())  # 
# print(date_2.today())  #
"""
Subclass relationships:

object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime
"""


time_1 = datetime.time()
# print(time_1)

date_5 = date_3.strftime("%H:%M:%S")
# print("Time: ", date_5)

date_str = "5/5"
format_str = "%d/%m"
date_6 = datetime.datetime.strptime(date_str, format_str)
# print(date_6)

data_json = {
 "name": "Python 2022I",
 "type": "private_channel",
 "id": 1658432930,
 "messages": [
  {
   "id": 1,
   "type": "service",
   "date": "2022-09-30T12:03:21",
   "date_unixtime": "1664521401",
   "actor": "Python 2022I",
   "actor_id": "channel1658432930",
   "action": "create_channel",
   "title": "Python 2022I",
   "text": ""
   }
  ]
 }

format_str = "%Y-%m-%dT%H:%M:%S"
date_6 = datetime.datetime.strptime(data_json["messages"][0]["date"], format_str)
# print(data_json["messages"][0]["date"])
# print(date_6)

date_7 = datetime.date.fromtimestamp(int(data_json["messages"][0]["date_unixtime"]))
# print(date_7.weekday())