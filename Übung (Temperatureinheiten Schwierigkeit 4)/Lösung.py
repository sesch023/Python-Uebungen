while True:
    print("1 - Celsius")
    print("2 - Fahrenheit")
    print("3 - Kelvin")
    print("ende - Beenden")
    print()

    eingabe = input("Bitte wählen Sie etwas aus: ")

    if eingabe == "ende":
        break

    temperatur = float(input("Bitte geben Sie den Temperaturwert an: "))

    if eingabe == "1":
        celsius = temperatur
        fahrenheit = (celsius * 9.0 / 5.0) + 32.0
        kelvin = celsius + 273.15
    elif eingabe == "2":
        fahrenheit = temperatur
        celsius = 5.0/9.0 * (fahrenheit - 32.0)
        kelvin = celsius + 273.15
    else:
        kelvin = temperatur
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9.0 / 5.0) + 32.0

    print("Celsius: " + str(celsius))
    print("Fahrenheit: " + str(fahrenheit))
    print("Kelvin: " + str(kelvin))
    print()



