# from IPython.display import clear_output

house_choices = {}
class House:

    def __init__(self, name):
        self.name = name
        self.price = None
        self.mortgage = 0

    def addMortgage(self):
        while True:
            ask_mortgage = input("Do you need a mortgage for this property? [yes] [no]: ")
            if ask_mortgage == 'yes':
                principal_loan_ammount = int(input("What is your principal loan ammount?: "))
                length_of_loan = int(input("What is the length of your loan in years?: "))
                interest_rate = float(input("What is the interest rate of your loan? (do not include the '%' symbol): ")) / 100
                monthly_interest_rate = interest_rate /12
                total_months = length_of_loan * 12
                n = total_months
                p = principal_loan_ammount
                i = monthly_interest_rate
                monthly_mortgage_payment = p*(i*((i+1)**n))/((1+i)**(n-1)) 
                print(f"At {interest_rate * 100}% interest rate, your monthly mortgage payment is ${monthly_mortgage_payment}")
                self.mortgage = monthly_mortgage_payment 
                break
            elif ask_mortgage == 'no':
                self.mortgage = 0
                break
            else:
                print("Not a valid response... ")
                continue

class CashFlow(House):

    def __init__(self, name):
        super().__init__(name)
        self.income = {}
        self.expenses = {'monthly mortgage payment': self.mortgage}
    
    def addIncome(self):
        go = True
        while go == True:
            print("Add Income Source")
            print("=================")
            income_type = input("What is the income from? i.e. rent, laundry, etc. : ")
            if income_type in self.income:
                print(f"{income_type} already added, please add a new one...")
                continue
            else:
                income_payment = int(input("What is the monthly payment from that income source? "))
                self.income[income_type] = income_payment
                # clear_output()
                
                while True:
                    add_income = input("Would you like to add another income source from the property? [yes] [no] ")
                    if add_income.lower() == 'yes':
                        # clear_output()
                        break
                    elif add_income.lower() == 'no':
                        # clear_output()
                        print(self.income)
                        go = False
                        break
                    else:
                        print("Not a valid response... please type 'yes' or 'no' ")
        house_choices[self.name]['income'] = self.income
    def addExpenses(self):
        go = True
        while go == True:
            print("Add Expense")
            print("============")
            expense = input("What is the expense for? (MORTGAGE ALREADY CALCULATED) i.e. utilities, tax, etc. : ")
            if expense in self.expenses:
                print(f"{expense} already added, please add a new one...")
                continue
            else:
                cost = int(input(f"What is the monthly cost of {expense.upper()}? "))
                self.expenses[expense] = cost
                # clear_output()
                
                while True:
                    add_expense = input("Would you like to add another expense? [yes] [no] ")
                    if add_expense.lower() == 'yes':
                        break
                    elif add_expense.lower() == 'no':
                        # clear_output()
                        print(self.expenses)
                        go = False
                        break
                    print("Not a valid response...")
        house_choices[self.name]['expenses'] = self.expenses
    def calcROI(self):
        total_income = 0
        total_expenses = 0
        for income_value in self.income.values():
            total_income += income_value
        
        for expense_value in self.expenses.values():
            total_expenses += expense_value 
        monthly_cash_flow = total_income - total_expenses

        print(f"Your monthly cash flow for this rental property is ${monthly_cash_flow}")
        
        cash_upfront = int(input("How much 'cash' did you put into buying this property? may include down payment, closing costs, rehab fees etc."))
        cash_on_cash_roi = (monthly_cash_flow*12)/cash_upfront * 100
        print(f"Your cash on cash ROI is {cash_on_cash_roi}%")    
        house_choices[self.name]['roi'] = cash_on_cash_roi

def run():
    while True:
        response = input("""
        What would you like to do?
        ===========================================
        [1] Analyze a new rental property
        [2] Compare your current rental properties
        [3] Done
        ===========================================
        """)
        if response == '1':
            house_name = input("what would you like to call this property?: ").title()
            house_price = int(input("What is the price of this property? no commas or '$' symbol: "))
            house_choices[house_name] = {'Price': house_price}
            house_name = CashFlow(house_name)
            house_name.addMortgage()
            house_name.addIncome()
            house_name.addExpenses()
            house_name.calcROI()

        
        elif response == '2':
            for house in house_choices.keys():
                print(house.title())
                print('===============')
                print(f"Price: ${house_choices[house]['Price']}")
                print('\nIncome')
                print('=========')
                for income in house_choices[house]['income']:
                    print(f"{income.title()}: ${house_choices[house]['income'][income]}")
                print("Expenses")
                print('=========')
                for expense in house_choices[house]['expenses']:
                    print(f"{expense.title()}: ${house_choices[house]['expenses'][expense]}")
                
                print(f"\nCash on Cash ROI: {house_choices[house]['roi']}%")
                print('--------------------')
        elif response == '3':
            break
        else:
            # clear_output()
            print("Not a valid command try again")
run()

