# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Joel Halnan

'''
Input - Person's name, hourly wage, hours
Process - Calculate's normal wages, over-time wages, combined wages, taxes withheld, medical insurance withheld, and take home pay.
Output - The employee's name, regular wages, overtime wages, total wages, taxes withheld, insurance withheld, and take home pay.
'''

def main():
    # Defining inputs
    name = input("Please enter your name:")
    hourlyWage = eval(input("Please enter your hourly wage:"))
    regularHoursWorked = eval(input("Please enter the number of hours worked:"))

    # Setting overtime to zero
    overTimeHours = 0
    
    # Calculations
    if regularHoursWorked > 40:
        overTimeHours = regularHoursWorked - 40
        regularHoursWorked = 40

    normalWage = regularHoursWorked * hourlyWage
    overTimeWage = overTimeHours * (hourlyWage * 1.5)
    totalWages = normalWage + overTimeWage
    taxWithheld = totalWages * .2
    insurance = totalWages * .1
    netPay = totalWages - taxWithheld - insurance

    # Output Section

    print ()
    print ("Name:\t\t\t", name)
    print ("Regular Wages:\t\t{0:.2f}".format(normalWage,2))
    print ("Overtime Wages:\t\t{0:.2f}".format(overTimeWage,2))
    print ("TOTAL WAGES:\t\t{0:.2f}".format(totalWages,2))
    print ()
    print ("Taxes Withheld:\t\t{0:.2f}".format(taxWithheld,2))
    print ("Insurance Withheld:\t{0:.2f}".format(insurance,2))
    print ()
    print ("Take home pay:\t\t{0:.2f}".format(netPay,2))
    print ()
    
    


#{0:.2f} 

main()