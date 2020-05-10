eshi = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
day  = int(input())
day = day + 4
day = day % 12
print(eshi[day])

