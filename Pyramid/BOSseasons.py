month = int(input("Enter the number of month: "))
if month <= 6 and month >= 4:
	print("Boston is in Spring.")
elif month <= 9 and month >= 7:
	print("Boston is in Summer.")
elif month <=11 and month >= 10:
	print("Boston is in Autumn.")
elif month <=3 or month == 12:
	print("Boston is in Winter.")
else:
	print("There are only 12 months in a year.")
