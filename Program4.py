#-------------------------------------------------------
#Author: Nicholas S, Billy P, Cooper W, Jacob T
#Program 2
#
#Description:
#A program created to allow a company to determine the amount
#of money owed to their employees based on their hours worked in a month and
#their pay rate (including a 5% bonus on overtime). Extra defense has been
#added to prevent the user from causing the program to fail as well as the
#ability to enter multiple employees in the same session. Now, all inputs are
#organized in functions written in BillingModule.py


#-------------------------------------------------------
import BillingModule


def runBillingReport():
#Named constants----
    OT_REQUIREMENT = 160
    WORK_WEEKS = 4
    OT_BONUS = 1.05
    another = 'y'
    
    #Resets the Billing.txt File every time the Entry Program is ran
        
    BillingModule.resetBillingFile()

    while another == 'y':
        
        #inputs----
        employee = BillingModule.readEmployeeName('\nEmployee Name: ')
      
        rate = BillingModule.readHourlyRate('Hourly Rate: ')    
        week1 = BillingModule.readWeeklyHours("Enter Hours Worked For Week 1: ")
        week2 = BillingModule.readWeeklyHours("Enter Hours Worked For Week 2: ")
        week3 = BillingModule.readWeeklyHours("Enter Hours Worked For Week 3: ")
        week4 = BillingModule.readWeeklyHours("Enter Hours Worked For Week 4: ")
        

        #Processing: Calculating pay and overtime----
        totalHours = week1+week2+week3+week4
        averageHours = totalHours / WORK_WEEKS
        otWorked = totalHours > OT_REQUIREMENT
        otRate = round(rate * OT_BONUS, 2)

        if otWorked:
            otHours = totalHours - OT_REQUIREMENT
            otPay = round(otHours * otRate, 2)
            otDisplay = (f"{employee} worked {otHours} hours of overtime.")
            otCalculation = (f"\nOvertime hours: {otHours:.2f} @ ${otRate:,.2f} = ${otPay:,.2f}")
        else:
            otHours = 0
            otPay = 0
            otDisplay = (f"{employee} worked no overtime.")
            otCalculation = ""

        regHours = totalHours - otHours
        regularPay = regHours * rate
        totalPay = regularPay + otPay


        BillingModule.writeBillingRecord(employee,str(rate),str(week1),str(week2),str(week3),str(week4)) #Data is written to file


        #Output: Print invoice----
        print(f"\n{otDisplay}")
        print("\nInvoice")
        print(f"Resource: ",employee,"\tAverage weekly hours: ", format(averageHours, '.2f'))
        print(f"\nTotal billable hours: {totalHours:.2f}\trate: ${rate:,.2f}", otCalculation)
        print(f"Regular Hours: {regHours:.2f} @ ${rate:,.2f} = ${regularPay:,.2f}")
        print(f"Amount Due: ${totalPay:,.2f}")

        another = input('\nWould you like to add another employee? (y = yes): ')
        print ('\n')
