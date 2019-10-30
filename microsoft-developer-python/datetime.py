#import datetime
from datetime import datetime, timedelta

#now function returns a datetime object
today = datetime.now()

#timedelta defines period of time
one_day = timedelta(days=1)
yesterday = today - one_day

print(f"Today is: {str(today)}")
print(f"Day: {str(today.day)}")
print(f"Month: {str(today.month)}")
print(f"Year: {str(today.year)}")
print(f"Hour: {str(today.hour)}")
print(f"Minute: {str(today.minute)}")
print(f"Second: {str(today.second)}")

birthday = input("When is your birthday (dd/mm/yyyy)? ")

birthday_date = datetime.strptime(birthday, "%d/%m/%Y")

print(f"Birthday = {str(birthday_date)}")
