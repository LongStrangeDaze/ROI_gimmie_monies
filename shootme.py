class Money:
    def __init__(self):
        self.gross = {}
        self.expenses = {}
        self.investments = {}

    def gross(self):
        gross_sources = input("How much do you make a year? ")
        gross_sources_exp = int((input(f"How much {gross_sources} do you get a month? ")))
        self.gross[gross_sources] = gross_sources_exp
    
    def expenses(self):
        expense_sources = input("What are your Expenses? ")
        expense_sources_exp = int((input(f"How much does {expense_sources} cost you every month? ")))
        self.expenses[expense_sources] = expense_sources_exp

    def investments(self):
        investment_sources = input("What is one major investment you have? ")
        investment_sources_exp = int((input(f"How much did you pay for {investment_sources}? ")))
        self.investments[investment_sources] = investment_sources_exp

    def show(self):
        user_input = input("Enter 1 to see your list of grosss, 2 to see your list of expenses, or 3 to see your list of investments ")
        if user_input == "1":
            print(self.gross)
        elif user_input == "2":
            print(self.expenses)
        elif user_input == "3":
            print(self.investments)
        else:
            print("Please choose a valid option!")
    
    def modify_elements(self):
        user_input = input("Enter 1 to modify your list of grosss, 2 for your list of expenses, or 3 for your list of investments ")
        if user_input == '1':
            gross_key = input("What source of gross would you like to change? ")
            for i in self.gross.keys():
                if gross_key == i:
                    gross_value = int(input("What do you want to change that cost to? "))
                    self.gross[i] = gross_value
        if user_input == '2':
            expense_key = input("What source of expense would you like to change? ")
            for x in self.expenses.keys():
                if expense_key == x:
                    expense_value = int(input("What do you want to change that cost to? "))
                    self.expenses[x] = expense_value
        if user_input == '3':
            investment_key = input("What source of investment would you like to change? ")
            for y in self.investments.keys():
                if investment_key == y:
                    investment_value = int(input("What do you want to change that cost to? "))
                    self.investments[y] = investment_value       

class Calculator(Money):
    def cash_flow_calc(self):
        annual_cash_flow = (sum(self.gross.values()) - sum(self.expenses.values())) * 12
        return annual_cash_flow

    def calculator_for_ROI(self):
        print(f"Your annual cash flow is {Calculator.cash_flow_calc(self)}.")

        total_investment_sum = sum(self.investments.values())
        roi_num = (Calculator.cash_flow_calc(self) / total_investment_sum) * 100
        print(f"Your ROI is {round(roi_num, 2)}%.")

obj1 = Calculator()
                     
def run():
    while True:
        user_input = input("""
            Looking to calculate your rental property's return on investment? We are happy to help here at Bigger Pockets!
            Choose the following: 
            1. Add a source of gross
            2. Add a source of expense
            3. Add an investment made for your property
            4. Modify
            5. Show the list of gross, expenses, and investments you have
            6. Calculate your ROI
            7. Quit/Exit
            """)
        if user_input == '7':
            print("Thanks for using our services...we'll bill you next time though!")
            break
        elif user_input == '1':
            obj1.gross()
        elif user_input == '2':
            obj1.expenses()
        elif user_input == '3':
            obj1.investments()
        elif user_input == '4':
            obj1.modify_elements()
        elif user_input == '5':
            obj1.show()
        elif user_input == '6':
            obj1.calculator_for_ROI()
        else:
            print("Please enter a valid number item 1-5 for the list of choices available")
run()