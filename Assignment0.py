
#This program converts Celsius to Fahrenheit and viceversa"
#It takes two inputs
#The temeperature and the unit it is in

unit = ('Celsuis')
unit2 = ('Fahrenheit')
temp = eval(input('Enter a temperature: ',))
user = input('Celsuis, Fahrenheit: ',)

if unit == user:
            print('In Fahrenheit: ', (9/5*temp)+32)
            
elif unit2 == user:
            print('In Celsuis: ', 5/9*(temp-32))
            
else:
    print("That is not a unit")
