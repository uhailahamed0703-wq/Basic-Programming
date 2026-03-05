Base_salary=5000000
Allowance=750000

BPJS_deduction = 0.02
Tax_deduction = 0.05

Salary=Base_salary + Allowance
BPJS_amount = Salary * BPJS_deduction
Tax_amount = Salary * Tax_deduction
Net_Salary = Salary - (BPJS_amount + Tax_amount)
print("The final salary is after deductions:", Net_Salary)