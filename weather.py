filename = "port-harcourt-weather.txt"

with open(filename) as file:
    file.next()
    next(file)
    dayList = []
    dailyTempSpread = []
    for line in file:
        line.strip()
        splitted_line = line.split()
        try:
            dayListNum = int(splitted_line[0])
            dailyHigh = int(splitted_line[1])
            dailyLow = int(splitted_line[2])
        except Exception as e:
            pass
        dailyTempSpread.append(dailyHigh - dailyLow)
        dayList.append(dayListNum)
weatherDict = dict(zip(dayList, dailyTempSpread))
print weatherDict
