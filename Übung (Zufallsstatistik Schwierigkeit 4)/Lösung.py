import random

values = []
for i in range(50):
    values.append(random.randrange(0, 51))

summe = 0
minimum = 51
maximum = 0

for value in values:
    summe += value
    if minimum > value:
        minimum = value
    if maximum < value:
        maximum = value

avg = summe / 50

print("Liste: " + str(values))
print("Arithmetisches Mittel: " + str(avg))
print("Minimum: " + str(minimum))
print("Maximum: " + str(maximum))
