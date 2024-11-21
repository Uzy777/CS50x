# FIX PRECISION ISSUES WITH CALCULATIONS USING FLOAT. SHOULD BE CONVERTING AND USING INTEGER!

while True:
    try:
        cents = float(input("Change owed: "))
        if cents >= 0:
            break
        else:
            print("Please enter a positive amount of change!")
    except ValueError:
        print("Please enter a valid value")

change = 0
# quarters = 0
# dimes = 0
# nickels = 0
# pennies = 0

while cents >= 0.25:
    cents = cents - 0.25
    change = change + 1

while cents >= 0.10:
    cents = cents - 0.10
    change = change + 1

while cents >= 0.05:
    cents = cents - 0.05
    change = change + 1

while cents >= 0.01:
    cents = cents - 0.01
    change = change + 1

print(change)
