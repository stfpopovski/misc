def salary_calcs():
    salary = input("Enter how much moneys this month: ")
    rent = input("Enter rent value: ")
    credit_value = 244.87
    savings = input("Enter how much savings are you going to put away: ")
    food = input("Enter how much money for food: ")
    total_expenses = float(rent) + credit_value + float(savings) + float(food)
    money_left = float(salary) - total_expenses
    print("Money left: ", round(money_left, 2))


salary_calcs()
