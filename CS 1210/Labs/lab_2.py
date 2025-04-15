#Excersise 1
KM_PER_PILE = 1.60934
def miles_to_km(miles):
    return miles * KM_PER_PILE

print(miles_to_km(0))     # should print 0.0
print(miles_to_km(100))   # should print 160.934
print(miles_to_km(5.25))  # should print 8.449035
print('\n')
#Excerise 2
def mpg(miles_driven,gas_consumed):
    return miles_driven/gas_consumed

print(mpg(50, 1))   # should print 50.0
print('\n')
#Excerise 3
def wind_chill(t,v):
    return 35.74+(0.6215*t)-(35.75*(v**(0.16)))+(0.4275*t)*(v**(0.16))

print(wind_chill(10,5)) #should print 1
print(wind_chill(-5,45)) #should print -37
print('\n')
#Excerise 4

print(wind_chill(18,14) - wind_chill(7,2))
print(wind_chill(7,2) - wind_chill(18,14))
print('You know the 18 degrees with 14mph winds is warmer than the 7 degrees with 2mph because when you subtract the 18,14 from the 7,2 you get a negative number, indicating that the 18,14 is a bigger number')