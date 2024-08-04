import locale
locale.setlocale(locale.LC_ALL, '')     # imports the local device's region, used in formatting currency

def readWeeklyHours(promptHours):    # reads the weekly hours
    MIN_HOURS = 35
    MAX_HOURS = 80
    again = True

    while again:
        try:
            weekHours = round(float(input(promptHours)), 2)
            if weekHours < MIN_HOURS or weekHours > MAX_HOURS:
                print('Invalid number of hours, must be between 35 and 80\n')
            else:
                again = False
        except ValueError:
            print('Please enter a numeric value.' + '\n')
            
    return weekHours

def readHourlyRate(promptRate):     # reads the hourly rate
    MIN_RATE = 20
    again = True

    while again:
        try:
            rate = round(float(input(promptRate)), 2)
            if rate < MIN_RATE:
                print('\nInvalid Hourly Rate, must be at least $20.00/hour')
            else:
                again = False
        except ValueError:
            print('Please enter a numeric value.' + '\n')
        
    return rate

def readEmployeeName(promptName):   # reads the employee name
    employee = input(promptName)
        
    while employee == '':
        print('Employee name must be entered')
        employee = input(promptName)
            
    return employee

def resetBillingFile():     # resets Billing.txt
    outfile = open('Billing.txt', 'w')

def writeBillingRecord(employee,rate,week1,week2,week3,week4):  # writes data to Billing.txt
    outfile = open('Billing.txt', 'a')
    outfile.write(employee+'\n')
    outfile.write(str(rate+'\n'))
    outfile.write(str(week1+'\n'))
    outfile.write(str(week2+'\n'))
    outfile.write(str(week3+'\n'))
    outfile.write(str(week4+'\n'))

def calcTotalPay(totalHours, rate, week1, week2, week3, week4):     # calculates total pay
    OT_REQUIREMENT = 160
    OT_BONUS = 1.05
    otWorked = totalHours > OT_REQUIREMENT
    otRate = round(rate*OT_BONUS, 2)
    
    if otWorked:
        otHours = totalHours - OT_REQUIREMENT
        otPay = round(otHours*otRate, 2)
        regularPay = OT_REQUIREMENT * rate
        totalPay = regularPay + otPay
    else:
        otHours = 0
        otPay = 0
        totalPay = (week1+week2+week3+week4)*rate
        

    return totalPay

def calcTotalHours(week1, week2, week3, week4):     # calculates total hours
    totalHours = week1 + week2 + week3 + week4
    
    return totalHours

def formatHours(totalHours):    # formats total hours
    totalHoursWorked = (locale.currency(float(totalHours), symbol = False))
    return totalHoursWorked


def formatCurr(currencyVar):    # formats currency values
    employeeRate = (locale.currency(float(currencyVar), grouping=True))

    return employeeRate

def calcTotalBillableDue(totalPay):     # formats total billable due
    totalBillableDue = totalPay

def printReportHeading():
    print('\n'+'Employee\t'+
        'Rate\t'+
        'Week1\t'+
        'Week2\t'+
        'Week3\t'+
        'Week4\t'+
        'Hours\t'+
        'Total')
