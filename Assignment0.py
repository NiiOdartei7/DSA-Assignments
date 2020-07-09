
#This program converts Celsius to Fahrenheit and viceversa"
#It takes two inputs
#The temeperature and the unit it is in

unit = ('Celsius')
unit2 = ('Fahrenheit')
temp = eval(input('Enter a temperature: ',))
user = input('Celsius, Fahrenheit: ',)

if unit == user:
            print('In Fahrenheit: ', (9/5*temp)+32)
            
elif unit2 == user:
            print('In Celsius: ', 5/9*(temp-32))
            
else:
    print("That is not a unit")
