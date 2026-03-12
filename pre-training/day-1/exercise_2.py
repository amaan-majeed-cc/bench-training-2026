# Write a function grade_classifier(score) that returns: 'Distinction' (90+), 'Pass' (60-89), 'Fail' (<60).
# Test it with at least 5 values. Then write a loop that runs through scores = [45, 72, 91, 60, 38, 85] and prints each result.
# Do not copy-paste the if-block 6 times. Use the function.

def grade_classifier(score):
  if score > 90:
    return 'Distinction'
  elif score < 89 and score > 60:
    return 'Pass'
  else:
    return 'Fail'

for score in [35, 42, 67, 95, 36, 58]:
  print(f'Score - {score}, Grade - {grade_classifier(score)}')

print('*' * 15)

for score in [45, 72, 91, 60, 38, 85]:
  print(f'Score - {score}, Grade - {grade_classifier(score)}')
