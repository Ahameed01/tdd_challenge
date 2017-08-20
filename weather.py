
# Assume the attached file port-harcourt-weather.txt contains weather data for
# Port Harcourt in 2016.  Download this file and write a program that returns the
# day number (column one) with the smallest temperature spread (the maximum
# temperature is the second column, the minimum the third column).


filename = "port-harcourt-weather.txt"

def weatherReport():
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


weatherReport()
