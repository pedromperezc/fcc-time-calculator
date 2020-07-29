def add_time(time, duration, day='Rola Grossa'):
	import math
	clock, period = time.split()
	hours, minutes = clock.split(":")

	add_hours, add_minutes = duration.split(":")

	# converting the hours into minutes and casting the minutes
	total_minutes_std_hour = (int(hours.strip()) * 60)
	total_minutes_add_hours = (int(add_hours.strip()) * 60)
	std_minutes = int(minutes.strip())
	add_minutes = int(add_minutes.strip())

	# total of hours combined
	total_minutes = int(total_minutes_std_hour + total_minutes_add_hours + std_minutes + add_minutes) 
	total_minutes_left = int((total_minutes_std_hour + total_minutes_add_hours + std_minutes + add_minutes) % 60)
	total_hours = total_minutes / 60

	# defining a standard for AM and PM
	periods = 0

	if period == "AM":
		periods = 0
	else:
		periods = 1

	# counting the number of periods
	periods += math.ceil(total_hours / 12)	

	# defining the specific printing period of the clock
	indicator_of_period = 0
	if periods % 2 != 0:
		indicator_of_period = "AM"
	else:
		indicator_of_period = "PM"

	# data that will be printed in the clock
	clock_minutes = total_minutes_left

	if clock_minutes < 10:
		clock_minutes = '0' + str(clock_minutes)

	clock_hour = total_hours
	days = periods / 2
	day_message = 0


	if clock_hour >= 12:
		clock_hour = clock_hour % 12
	
		if indicator_of_period == "PM" and int(clock_hour) == 0:
			clock_hour = 12

	if float(days) < 1:
		day_message = "Same day"

	elif float(days) > 1 and days <= 2: 
		day_message = "(next day)"

	else:
		day_message = str(math.ceil(days)) + " days later)"

	days = math.floor(periods / 2)

	days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday")

	if day not in days_of_the_week:		
	
		returning_data = str(int(clock_hour)) + ":" + str(clock_minutes) + " " + indicator_of_period + " (" + day_message

		return (returning_data)

	
	elif day in days_of_the_week:
		if day == "Monday":
			day = (1 + days) % 7
			day = days_of_the_week[day]

		elif day == "Tuesday":
			day = (2 + days) % 7
			day = days_of_the_week[day]

		elif day == "Wednesday":
			day = (3 + days) % 7
			day = days_of_the_week[day]

		elif day == "Thursday":
			day = (4 + days) % 7
			day = days_of_the_week[day]

		elif day == "Friday":
			day = (5 + days) % 7
			day = days_of_the_week[day]


		elif day == "Saturday":
			day = (6 + days) % 7
			day = days_of_the_week[day]

		else: 
			day = days % 7
			day = days_of_the_week[day]

		returning_data = str(int(clock_hour)) + ":" + str(clock_minutes) + " " + indicator_of_period + " " + day + " (" + day_message

		return returning_data



