from datetime import datetime

# creating object

obj_now = datetime.now()
greeting = ''

# printing the current date and time

# print("current date & time: ", obj_now)

# Extracting and printing the current
# hour,minute,second,microsecond

# print("current hour =", obj_now.hour)
# print("current minute =", obj_now.minute)
# print("current second =", obj_now.second)
# print("current microsecond =", obj_now.microsecond)

my_hours = obj_now.hour
# my_hours = 17
# print(my_hours)


if (my_hours > 6 and my_hours < 12):
    greeting = "Good Morning"
elif (my_hours >= 12 and my_hours < 17):
    greeting = "Good Evening"
elif (my_hours >= 17 and my_hours < 23):
    greeting = "Good Night"

print("Hello Hamna,", greeting)