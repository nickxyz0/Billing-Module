import locale
locale.setlocale(locale.LC_ALL, '')   # imports the local device's region, used in formatting currency

import BillingModule

def writeAdHocReport():
    try:
        infile = open('Billing.txt', 'r')
        BillingModule.printReportHeading()
        
    except FileNotFoundError:
        BillingModule.printReportHeading()
        print('No Employees On File.')
        
    else:
        employee = infile.readline().rstrip('\n')
        numEmployees = 0
        totalBillableHours = 0.00
        totalBillableDue = 0.00

        while employee != '':
            rate = infile.readline().rstrip('\n')
            week1 = infile.readline().rstrip('\n')
            week2 = infile.readline().rstrip('\n')
            week3 = infile.readline().rstrip('\n')
            week4 = infile.readline().rstrip('\n')

            totalHours = BillingModule.calcTotalHours(float(week1),float(week2),float(week3),float(week4))
            totalPay = BillingModule.calcTotalPay(float(totalHours), float(rate), float(week1), float(week2), float(week3), float(week4))
            numEmployees += 1

            employeeRate = BillingModule.formatCurr(rate)
            empWeek1 = BillingModule.formatHours(week1)
            empWeek2 = BillingModule.formatHours(week2)
            empWeek3 = BillingModule.formatHours(week3)
            empWeek4 = BillingModule.formatHours(week4)
            totalHoursWorked = BillingModule.formatHours(totalHours)
            empTotalPay = BillingModule.formatCurr(totalPay)

            totalBillableHours = totalBillableHours + totalHours
            totalBillableDue = totalBillableDue + totalPay

            print(employee+'\t'+
                  str(employeeRate)+'\t'+
                  str(empWeek1)+'\t'+
                  str(empWeek2)+'\t'+
                  str(empWeek3)+'\t'+
                  str(empWeek4)+'\t'+
                  str(totalHoursWorked)+'\t'+
                  str(empTotalPay))

            employee = infile.readline().rstrip('\n')

        infile.close()

        avgBillableHours = (totalBillableHours/4)/numEmployees
        print('\nTotal Billable Due:\t' + str(BillingModule.formatCurr(totalBillableDue)))
        print('Total Billable Hours:\t' + str(BillingModule.formatHours(totalBillableHours)))
        print('Average Billable Hours:\t' + str(BillingModule.formatHours(avgBillableHours)))
