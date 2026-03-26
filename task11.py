def calculate_tax(salary: float) -> float:
    if salary > 5_000_000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary: float) -> float:
    return salary - calculate_tax(salary)


salary = float(input("Maosh kiriting: "))

tax = calculate_tax(salary)
net = calculate_net_salary(salary)

print(f"Soliq: {tax}")
print(f"Sof maosh: {net}")