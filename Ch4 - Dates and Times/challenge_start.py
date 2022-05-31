# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
# 1. Print the string asking user to choose the day of the week and then the month and year for which count of the day is required
# 2. Make sure the selection is from a fixed set of strings. 
# 3. Send the information to another class - where count of days is calculated
# 4. 

import calendar
def countdays(theyear, themonth, whichday):
    daycount = 0
    weekslist = calendar.monthcalendar(theyear, themonth)
    for week in weekslist:
        if week[whichday] != 0:
            daycount += 1
    return daycount

run = True
while (run):
    i = 0
    print("Select the day of the week or type exit to quit:")
    for day in calendar.day_name:
        print (i, day)
        i = i+1
    weekselect = input("Your selection: ")
    
    lower_testchar = weekselect.lower()
    if lower_testchar == "exit":
        run = False
        break
    elif weekselect.isnumeric() == False or int(weekselect) > i:
        print("Please add a valid number")
    else: 
        useryear = int(input("Enter year: "))
        usermonth = int(input("Enter month: "))
        #userday = calendar.day_name[int(weekselect)]
        userday = int(weekselect)
        print(userday)
        result = countdays(useryear, usermonth, userday)

        print("There are "+ str(result) +" in the month of specified year.")
        # i = calendar.weekday(useryear, usermonth, int(weekselect)-1)
        # print (i)


