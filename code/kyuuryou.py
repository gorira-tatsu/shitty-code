print("時給[1]、日[2]、月[3]、年[4]数字で指定してください")
unit = int(input())
print("働く時間を指定してください")
time = int(input())
print("時間の単位でもらえるお金を指定してください")
monay = int(input())

if unit == 1:
	monay = monay * time
	print("その時間でもらえるお金は....")
	print(monay)

elif unit == 2:
	monay = monay * time * 24
	print("その時間でもらえるお金は....")
	print(monay)

elif unit == 3:
	monay = monay * time * 24 * 30
	print("その時間でもらえるお金は....")
	print(monay)

elif unit == 4:
	monay = monay * time * 24 * 30 * 12
	print("その時間でもらえるお金は....")
	print(monay)





