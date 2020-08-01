limit = int(input("Bitte geben sie eine natürliche Zahl an: "))

counter = 1
sum = 0
while counter <= limit:
    sum += counter
    counter += 1

print(f"Die Summe aller natürlicher Zahlen bis {str(limit)} ist {str(sum)}!")
