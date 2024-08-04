import Program4, Program5, BillingModule

def main():
    showMenu = 'True'
    while showMenu == 'True':
        try:
            print('\nBilling System Menu: ')
            print('\n\t0 - End')
            print('\t1 - Enter Billing Data')
            print('\t2 - Display adhoc billing report'+'\n')

            answer = int(input('Option ==> '))


            if answer == 0:
                showMenu = 'False'
            elif answer ==1:
                Program4.runBillingReport()
            elif answer ==2:
                Program5.writeAdHocReport()
            else:
                print('Invalid Option.')
        except ValueError:
            print('Invalid Option.')
    print('\nBilling Program ended')

main()
