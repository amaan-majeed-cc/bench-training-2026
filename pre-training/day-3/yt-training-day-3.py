
class Employee:
  num_of_emps = 0
  raise_amount = 1.04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first.lower() + '.' + last.lower() + '@gmail.com'

    Employee.num_of_emps += 1

  def fullname(self):
    return f'{self.first} {self.last}'

  def apply_raise(self):
    self.pay *= self.raise_amount

  @classmethod
  def set_raise_amt(cls, amount):
    cls.raise_amount = amount

  @staticmethod
  def is_workday(date):
    import datetime

    if date.weekday() == 6 or date.weekday() == 6:
      return False
    return True

class Developer(Employee):
  def __init__(self, first, last, pay, prog_lang):
    super().__init__(first, last, pay)
    self.prog_lang = prog_lang

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)


# emp_1.first = 'Taha'
# emp_1.last = 'Yasin'
# emp_1.email = 'taha.yasin@gmail.com'
# emp_1.pay = 50_000

# emp_2.first = 'Muhammad'
# emp_2.last = 'Awais'
# emp_2.email = 'muhammad.asn@gmail.com'
# emp_2.pay = 40_000

# print(emp_1.email)
# print(emp_2.email)


# emp_1 = Employee('Taha', 'Yasin', 50_000, )
# emp_2 = Employee('Muhammad', 'Ans', 40_000)

# print(emp_1.pay)
# print(emp_2.pay)
# print(emp_1.fullname())

# emp_1.apply_raise()

# print(emp_1.pay)
# print(emp_2.pay)
# print(Employee.num_of_emps)


dev_1 = Developer('Taha', 'Yasin', 50_000, "Java")
dev_2 = Developer('Muhammad', 'Ans', 40_000, "Python")

print(dev_1.email)
print(dev_1.prog_lang)


print(isinstance(dev_2, Developer))
print(issubclass(Developer, Employee))
