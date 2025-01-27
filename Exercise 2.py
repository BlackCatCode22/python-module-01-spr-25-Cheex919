
input_hours = input('Enter Hours: ')
input_rate = input('Enter Rate: ')
hours = float(input_hours)
rate = float(input_rate)
overtime_rate = 1.5

if hours <= 40:
    pay = rate * hours
else:
    pay = ((hours - 40) * (overtime_rate)) + (40 * rate)

print('Pay: ', pay)