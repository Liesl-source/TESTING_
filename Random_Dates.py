import time

import random

def getRandomDate(startDate, endDate):

# Use correct date format -> %m/%d/%Y for 4-digit year

    dateFormat = "%m/%d/%Y"


# Convert start and end date strings to time objects

    startTime = time.mktime(time.strptime(startDate, dateFormat))

    endTime = time.mktime(time.strptime(endDate, dateFormat))


# Generate random timestamp between start and end

    randomTime = startTime + random.random() * (endTime - startTime)


# Convert random timestamp back to formatted date string

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))


    return randomDate

# Display result

print("Random Date is:", getRandomDate("1/1/2016", "12/12/2018"))