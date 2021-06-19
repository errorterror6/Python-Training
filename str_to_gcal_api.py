from datetime import datetime

date_month = "08/06"
year = "/21"
time = " 09:00:00"

date_time_str = date_month + year + time
print("test" + date_time_str)

date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')

date_time_test = date_time_obj.strftime("%y-%m-%dT%H:%M:%S")
API_date_time = str(date_time_test) + "+10:00"
print(API_date_time)



print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)