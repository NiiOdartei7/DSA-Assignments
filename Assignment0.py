
#This program converts Celsius to Fahrenheit and viceversa"
#It takes two inputs
#The temeperature and the unit it is in
#The output is the converted temperature value


unit = ('Celsius')
unit2 = ('Fahrenheit')
temp = eval(input('Enter a temperature: ',))
user = input('Is it in Celsius or Fahrenheit (Enter the unit only): ',)

if unit == user:
            print('In Fahrenheit it is: ', (9/5*temp)+32)
            
elif unit2 == user:
            print('In Celsius it is: ', 5/9*(temp-32))
            
else:
    print("That is not a unit")
