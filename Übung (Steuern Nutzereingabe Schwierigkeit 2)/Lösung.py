einkommen = float(input("Bitte geben Sie ihr Einkommen in Euro an: "))
vermoegen = float(input("Bitte geben Sie ihr Vermögen in Euro an: "))

steuer_einkommen = 0.05
steuer_vermoegen = 0.01

if 20000 <= einkommen < 40000:
    steuer_einkommen = 0.15
elif 40000 <= einkommen < 100000:
    steuer_einkommen = 0.25
elif einkommen >= 10000:
    steuer_einkommen = 0.4

if 10000 <= vermoegen < 50000:
    steuer_vermoegen = 0.03
elif 50000 <= vermoegen < 200000:
    steuer_vermoegen = 0.05
elif vermoegen >= 200000:
    steuer_vermoegen = 0.1

steuer = steuer_einkommen * einkommen + steuer_vermoegen * vermoegen
print("Steuer: " + str(steuer))
