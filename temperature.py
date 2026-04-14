def convert(fahrenheit):
    celcius=(5/9)*(fahrenheit-32)
    return celcius
f=float(input("Enter the temperature in Fahrenheit: "))
c=convert(f)
print("Temperature in celcius: ", c)
if c > 20:
    print("IT'S HOT HERE")
else:
    print("ITS'S COLD HERE")
