salary = float(input("Enter employee's salary: "))
percentage = int(input("Enter percentage of salary increase: "))
percentage_salary = (percentage/100) * salary
increase_salary = salary + percentage_salary
print("This employee receives the salary amount of {},but adding {} % of increase,it goes actually to {:.2f} of total salary. ".format(salary,percentage,increase_salary))