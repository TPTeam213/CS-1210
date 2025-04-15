'''
Ben Frederick
CS 1210
'''

def calc_tax(income):
    tax = 0
    if income >= 0:
        tax += min(income, 11000) * .10
    if income > 11000 :
        tax += (min(income, 44725) - 11000) * .12
    if income > 44725:
        tax += ((min(income, 95375)) - 44725) * .22
    if income > 95375:
        tax += ((min(income, 182100)) - 95375) * .24
    if income > 182100:
        tax += ((min(income, 231250)) - 182100) * .32
    if income > 231250:
        tax += ((min(income, 578125)) - 231250) * .35
    if income > 578125:
        tax += (income - 578125) * .37
    return tax

if __name__ == '__main__':
    income = int(input('Enter your taxable income $: '))
    taxx = calc_tax(income)
    print(f'Tax on ${income:,} is ${taxx:,.0f}.')