# This was a code created for a project done for ANL251 Python Programming
print("""\nWelcome to the Standard Chartered Bank Bonus$aver interest rate calculator
-----------------------------------------------------------------------------

Use this calculator to determine out how much interest you can earn per month
with the Bonus$aver Account.

""")

#while loop to allow users to try again
while True:
    try:
        #First input: Average daily balance
        while True: #While-loop to allow users to ensure that users enter the correct value
            try:
                balance = float(input("Please enter your estimated Bonus$saver average daily balance: ")) #input function/validate data type
                if balance < 2000: #minimum acc balance must be $2000 to be eligible
                    print("Sorry. You must have a minimum balance of S$2,000.00 to be eligible for the Bonus$aver annual interest") #error message to tell them insufficient balance
                    tryagain = input("Do you want to enter another daily balance?\n\nPress y to try again.\nPress any key to quit.") #cue them to reenter or stop prog
                    if tryagain.lower() == 'y': #try again, loops back to input balance
                        continue
                    else: #any other key will break off the loop and stop programme
                        print("\nThank you for using the Bonus$aver Calculator!") #courtesy sake
                        exit() #exits script if user does not want to try again
                else:
                    print(f"Your estimated Bonus$aver average daily balance is ${balance:.2f}. ")
                #print to show how much user entered
            except ValueError: #if user enter anything other than numbers
                print("You have entered an invalid response.\nPlease try again.")
                continue
            else: #successfully entered, time to come out of loop
                break
        total_int = [] #using list to accumulate interest as the calculator goes on
        #Second input: estimated monthly card spending, 0 in list
        while True:
            try:
                spend = float(input("\nPlease enter your estimated monthly card spending: ")) #ensure that options are only int
                if spend < 500:
                    total_int.append(0)# adds on to list as the location 0, 0% interest for < 500
                    print(f"Sorry, your spending of S${spend:.2f} falls under the minumum required spending of S$500.00 to be eligible for the spending interest")
                elif spend >= 500 and spend < 2000:
                    total_int.append(0.3) # 0.3% interest for 500 - 2000
                    print(f"You will receive an extra {total_int[0]:.2f}% annual interest from your estimated monthly card spending.")
                elif spend >= 2000:
                    total_int.append(0.8) # 0.8% interest for >= 2000
                    print(f"You will receive an extra {total_int[0]:.2f}% annual interest from your estimated monthly card spending.")
            except ValueError:
                print(f"You have entered an invalid response.\nPlease try again.")
                continue #make user re-enter another option if a wrong option is selected
            else:
                break #moving on after user enters the correct value
        #third input: Salary credit, 1 in list
        while True:
            try:
                salary = float(input("\nPlease input the monthly salary to be credited into the Bonus$aver account: "))
                if salary >= 3000:
                    total_int.append(0.4) #adds on to location 1 in total_int list, 0.4% if salary quota hit
                    print(f"You will receive an extra {total_int[1]:.2f}% annual interest for crediting a salary of more than S$3,000.") #reflects interest earned
                else:
                    total_int.append(0) #adds on to location 1 in total_int list, 0 if not hit
                    print(f"Sorry, your salary credit of S${salary:.2f} falls under the minumum required amount of S$3,000.00 to be eligible for the salary credit interest.") #reflects no int earn
            except ValueError :
                print(f"You have entered an invalid response.\nPlease try again.") #check for wrong value
                continue
            else:
                break #option entered, come out of loop
        #Fourth input: Invest, 2 in list
        answery = "y" #for y/n questions, yes reply
        answern = "n" #no reply
        while True:
            try:
                invest = str(input("\nWill you invest through us in eligible products?\nY/N? ")) #Fourth input: Invest or no?
                if invest.lower() == answery: #if y chosen, will assess the input amount, .lower() is used in case CAPS is used
                    invest_amt = float(input("Please enter the amount that you will invest: "))
                    while True: #justify the investment amount only after user select that investment to be done
                        try: #assess the investment amount
                            if invest_amt >= 30000: #above 30,000 to qualify for 0.85
                                total_int.append(0.85)
                                print(f"You will receive an extra {total_int[2]:.2f}% annual interest for investing in eligible products")
                            else:
                                total_int.append(0) #anything below disqualify
                                print(f"Sorry, your investment amount of S${invest_amt:.2f} falls under the minumum ticket size of S$30,000.00 to be eligible for the investment interest")
                        except ValueError: #if they enter anything other than float amount
                            print("You have entered an invalid response.\nPlease try again.")
                            continue
                        else:
                            break
                elif invest.lower() == answern: #if n is chosen. consider as 0 int
                    total_int.append(0)
                    print("Sorry, you will not be eligible for the interest earned from investing in eligible products.")
                else: #limit answer to y or n
                    raise ValueError
            except ValueError:
                print(f"You have entered an invalid response.\nPlease try again.")
                continue
            else:
                break
        #Fifth Input: Insure? 3 in list
        while True:
            try:
                insure = str(input("\nWill you purchase an eligible insurance policy through us?\nY/N? "))
                if insure.lower() == answery: #if y chosen, will assess the input amount, .lower() is used in case CAPS is used
                    insure_amt = float(input("Please enter the annual premium that you will insure: "))
                    while True:
                        try: #assess the insurance amount
                            if insure_amt >= 12000:
                                total_int.append(0.85)
                                print(f"You will receive an extra {total_int[3]:.2f}% annual interest for insuring in eligible products")
                            else:
                                total_int.append(0) #anything below disqualify
                                print(f"Sorry, your minimum annual premium of S${insure_amt:.2f} falls under the minumum premium of S$12,000.00 to be eligible for the insurance interest")
                        except ValueError: #if they enter anything other than float amount
                            print("You have entered an invalid response.\nPlease try again.")
                            continue #cue to input float amt again
                        else:
                            break #out of loop when proper amt input
                elif insure.lower() == answern: #if n is chosen. consider as 0 int
                    total_int.append(0)
                    print("Sorry, you will not be eligible for the interest earned from insuring in eligible products.")
                else:
                    raise ValueError
            except ValueError:
                print(f"You have entered an invalid response.\nPlease try again.")
                continue
            else:
                break
        #Sixth Input: Bill payment? 4 in list
        while True:
            try:
                bill = str(input("\nWould you make at least 3 bill payments via GIRO or our Online Banking Platform?\nY/N? ")) #assess if they are paying bill via platform
                if bill.lower() == answery: #if yes, assess if qualified
                    bill_amt1 = float(input("Please input the bill amount to be paid for the 1st bill: ")) #3 bills to be assessed, thus 3 inputs
                    bill_amt2 = float(input("Please input the bill amount to be paid for the 2st bill: "))
                    bill_amt3 = float(input("Please input the bill amount to be paid for the 3rd bill: "))
                    if bill_amt1 >= 50 and bill_amt2 >= 50 and bill_amt3 >= 50: #aLL 3 bills must be above $50 to be eligible for interest
                        total_int.append(0.1)
                        print(f"You will receive an extra {total_int[4]:.2f}% annual interest for making 3 bill payments online.")
                    else:
                        total_int.append(0) #else not eligible, int = 0
                        print("Sorry. In order to receive extra annual interest from bill payments, you must make minimum 3 eligible bill payments which are more than S$50 per payment")
                elif bill.lower() == answern:
                    total_int.append(0) #if n, int = 0
                    print("Sorry, you will not be eligible for the interest earned from making bill payments.")
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"You have entered an invalid response.\nPlease try again.")
                continue
            else:
                break
        #Calculating total interest
        total_int_sum = sum(total_int) #sum of all interest inputs = total annual interest
        monthly_int = float(total_int_sum) / 12 #convert int into float type, and divide by 12 months for monthly interest
        def balance_max(maxn): #function is defined to ensure that regardless of input amt for balance, it maxes at maxn
            if balance > maxn:
                return maxn #return maxn if balance is more than maxn
            else:
                return balance
        balance = balance_max(80000) #as the total eligible balance is capped at 80,000, the max eligible fund is cap at 80,000. This can be changed when the policy changes
        total_int_amt = float(balance * (total_int_sum/100)) #amount of interest in $ earned as per input balance (up to 80,000)
        monthly_int_amt = float(total_int_amt/12) #monthly interest in $ as per input balance
        #summary of interests, individual, followed by annual and monthly. \n, \t and """ used to format output neatly
        print(f"""\nWith a balance of S${balance:.2f}, the summary of interest earned (p.a.) are as follows:
    Credit spending\t\t-->\t{total_int[0]:.2f}%
    Salary credit\t\t-->\t{total_int[1]:.2f}%
    Investment\t\t\t-->\t{total_int[2]:.2f}%
    Insurance\t\t\t-->\t{total_int[3]:.2f}%
    Bill Payment\t\t-->\t{total_int[4]:.2f}%\n""")
        print(f"Your estimated annual interest is: S${total_int_amt:.2f} @ {total_int_sum:.2f}% per annum.")
        print(f"Your estimated monthly interest is: S${monthly_int_amt:.2f} @ {monthly_int:.2f}% per month.")
        restart = input("\nDo you want to try again?\nPress Y to try again.\nPress any key to exit.") #prompt user to restart or end calculation
    except:
        if tryagain.lower() == 'y': #try again, loops back to input balance
            continue
        else: #any other key will break off the loop and stop programme
            exit() #exits script if user does not want to try again
    else:
        if restart.lower() == 'y': #if y, restart
            continue
        else:
            print("\nThank you for using the Bonus$aver Calculator!") #courtesy sake
            exit() #any key, exits
