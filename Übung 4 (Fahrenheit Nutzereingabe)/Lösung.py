fahrenheit = input("Bitte geben Sie einen Wert in Fahrenheit an: ")
fahrenheit = float(fahrenheit)

celsius = 5.0/9.0 * (fahrenheit - 32.0)
kelvin = celsius + 273.15

print("Fahrenheit: " + str(fahrenheit))
print("Celsius: " + str(celsius))
print("Kelvin: " + str(kelvin))
