"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hourly_pay=0, hours_worked=0, bonus_commissions=0, contract_commission=0, numberOf_contracts=0):
        self.name = name
        self.salary = salary
        self.hourly_pay = hourly_pay
        self.hours_worked = hours_worked
        self.bonus_commissions = bonus_commissions
        self.contract_commission = contract_commission
        self.numberOf_contracts = numberOf_contracts

    def get_pay(self):
        total = 0
        if self.salary:
            total += self.salary
        if self.hourly_pay:
            total += self.hourly_pay * self.hours_worked
        if self.bonus_commissions:
            total += self.bonus_commissions
        if self.contract_commission:
            total += self.contract_commission * self.numberOf_contracts
        return total

    def __str__(self):
        type = ""
        if self.salary:
            type += "monthly salary of " + str(self.salary)
        if self.hourly_pay:
            type += "contract of " + str(self.hours_worked) + " hours at " + str(self.hourly_pay) + "/hour"
        if self.bonus_commissions:
            type += " and receives a bonus commission of " + str(self.bonus_commissions)
        if self.contract_commission:
            type += " and receives a commission for " + str(self.numberOf_contracts) + " contract(s) at " + str(self.contract_commission) + "/contract"
        return (f'{self.name} works on a {type}.  Their total pay is {self.get_pay()}.')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(name = 'Billie', salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(name = 'Charlie', hourly_pay = 25, hours_worked = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(name = 'Renee', salary = 3000, contract_commission = 200, numberOf_contracts = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee(name = 'Jan', hourly_pay = 25, hours_worked = 150, contract_commission = 220, numberOf_contracts = 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(name = 'Robbie', salary = 2000, bonus_commissions = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(name = 'Ariel', hourly_pay = 30, hours_worked = 120, bonus_commissions = 600)



print(billie.__str__())
print(charlie.__str__())
print(renee.__str__())
print(jan.__str__())
print(robbie.__str__())
print(ariel.__str__())
