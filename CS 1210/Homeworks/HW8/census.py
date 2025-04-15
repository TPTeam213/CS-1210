''''
Ben Frederick
CS 1210
'''
import csv

if __name__ == '__main__':
    population = 0
    income = 0
    data = []

    state = input("Enter name of state: ").lower()
    filename = state.replace(" ", "_") + ".csv"
    with open(filename, 'r') as file:
        reading = csv.reader(file)
        next(reading)
        for row in reading:
            pop = int(row[4])
            pci = (int(row[1])) * pop
            population += pop
            income += pci
        avg_pci = income / population
    with open(filename, 'r') as file:
        reading = csv.reader(file)
        next(reading)
        for row in reading:
            if int(row[1]) > avg_pci:
                data.append(str(row[0]))
    
    state = state.title()
    print(f'The total population of {state} is {population:,}')
    print(f'{state} per capita income is ${avg_pci:,.0f}')
    print(f'The following counties have per capita income above the state average:')
    for i in data:
        print(i)