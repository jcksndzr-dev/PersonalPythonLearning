from time import sleep
import sys
import os

def numCruncher(amt, perc, split): 
    if amt >= 1000: ### We don't need rich people to use the tip calculator.
        print(f'''
---------------------------------------------
You are too fancy to use this calculator. 
Please go take your privilege somewhere else.
---------------------------------------------
''')
    else:      
        percent = perc / 100
        bill = round(amt,2)
        try: 
            if split > 1: ### How many people are splitting the bill?
                tip = round((bill / split) * percent, 2)
                splitAmount = round(bill / split, 2)
                totalAmountSplit = tip + splitAmount
                print(f'''
---------------------------------------------
    {'Group Bill:' :<15} ${bill:>15.2f}
    {'Your Bill:' :<15} ${splitAmount:>15.2f}
    {'Your Tip:' :<15} ${tip:>15.2f}
    {'Your Portion:' :<15} ${totalAmountSplit:>15.2f}
---------------------------------------------
                    ''')
                print("\n")
                banjo = input("Press enter to calculate a new tip, or type 'q' to quit: ")
                if banjo.lower() != 'q':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    tipCalcStart()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return exit()
            else:
                tip = round(bill * percent, 2)
                totalAmount = round(tip + bill, 2)
                print(f'''
---------------------------------------------
           Total Bill:   ${bill:.2f} 
                  Tip:   ${tip:.2f} 
           Your Total:   ${totalAmount:.2f}
---------------------------------------------
                ''')
                print(" ")
                banjo = input("Press enter to calculate a new tip, or type 'q' to quit: ")
                if banjo.lower() != 'q':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    tipCalcStart()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return exit()
        except Exception as e:
            print(f"Something went wrong. Please try again. Error {e}")


def tipCalcStart():
    print(f"\n\n")
    while True:
        billInput = input("How much is the total bill? ")
        if billInput == 'q' or billInput == 'Q':
            return exit()
        else:
            try:
                amt = float(billInput)
                if amt > 0:
                    break
                else: 
                    print(f'Your entry, ${format(round(amt, 2), ".2f")}, is invalid. Bill cannot be less than $0.00. Please enter the total bill.')
            except Exception as e:
                print(f'Your entry, {billInput}, is invalid. Bill cannot be less than $0.00. Please enter the total bill. Error {e}')

    while True:
        percInput = input("What percentage do you want to tip? ")
        if percInput == 'q' or percInput == 'Q':
            return exit()
        else:
            try:
                perc = float(percInput)
                if perc >= 5:
                    break
                else: 
                    print(f'Your entry, {percInput}, is rude. Tip should not be less than 5%. Please enter a tip percentage higher than 5%.')
            except Exception as e:
                print(f'Your entry, {percInput}, is invalid. Tip should not be less than 5%. Please enter a tip percentage higher than 5%. Error {e}')

    while True:
        splitInput = input("How many people are splitting the bill? ")
        if splitInput == 'q' or splitInput == 'Q':
            return exit()
        else:
            try:
                spl = int(splitInput)
                if spl > 0:
                    return numCruncher(amt, perc, spl)
                else:
                    print("Please enter the amount of people who are splitting the bill. If it is just you, please enter 1.")
            except Exception as e:
                print(f"Please enter the amount of people who are splitting the bill. If it is just you, please enter 1. {e}")

def welcome():
    os.system('cls' if os.name == 'nt' else 'clear') ### Clears screen before printing welcome
    print(f'''
          
          
---------------------------------------------     
        Welcome to the Tip Calculator. 
        Please follow the prompt below.
        Type "q" at any time to quit.
---------------------------------------------
          
          ''')
    tipCalcStart()

if __name__ == "__main__":    
    welcome()