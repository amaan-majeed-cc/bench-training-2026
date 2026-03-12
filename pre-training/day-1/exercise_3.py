# Build a multiplication table generator. Ask the user for a number (1–12), then print the full table.
# Format it so it looks clean — right-align numbers. If they enter something outside 1-12, tell them to try again (use a while loop).
# Bonus: make it print tables for ALL numbers 1-12 in a single run.

def table_generator(num):
  print("-" * 10, "Table of", num, "-" * 10)
  for i in range(1, 11):
    print(f'|{num:6} x {i:2} = {i * num:4}   |')


number = int(0)
while int(number) < 1 or int(number) > 12:
  number = int(input ('Enter a number between 1-12: '))

table_generator(number)

print('\n\n', '=' * 15, 'Bonus', '=' * 15, '\n\n')

for i in range(1, 13):
  table_generator(i)


