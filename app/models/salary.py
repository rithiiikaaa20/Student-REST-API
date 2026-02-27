from dataclasses import dataclass

@dataclass
class Salary:
    SalaryID: int
    EmployeeID: int
    BasicSalary: float
    Bonus: float
    Allowances: float
