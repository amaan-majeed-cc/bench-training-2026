# Create variables for: your name, age, whether you drink coffee (bool), your salary (float).
# Print a formatted sentence using all four. Then compute: years until retirement at 60, and weekly coffee budget if you drink 3 cups/day at Rs. 150 each.
# No hardcoding allowed — use variables everywhere.


name = str('Amaan Majeed')
age = int(24)
drink_coffee = bool(False)
salary = float(500_000.00)

print(f"Hello my name is {name}, I am {age} years old", end=" and ")
print("I drink coffee" if drink_coffee else "I don't drink coffee.")
print(f"I make {salary} per month.")

RETIREMENT_AGE = 60
DAILY_COFFEE_INTAKE = 3
PRICE_PER_COFFEE = 150
DAYS_IN_A_WEEK = 7

years_till_retirement = RETIREMENT_AGE - age
weekly_coffee_budget = DAILY_COFFEE_INTAKE * DAYS_IN_A_WEEK * PRICE_PER_COFFEE

print(f'I have {years_till_retirement} years left until I retire at the age of 60')
print(f'And My weekly Coffee Budget is Rs. {weekly_coffee_budget}')




