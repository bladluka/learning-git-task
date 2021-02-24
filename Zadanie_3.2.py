lista_zakupow = {'piekarnia': ['chleb', 'pączek', 'bułki'], 'warzywniak': ['marchew', 'seler', 'rukola']}
for number in lista_zakupow:
    print(f"Idę do {number.capitalize()} i kupuję tam {[number2.capitalize() for number2 in lista_zakupow.get(number)]}")
print(f"W sumie kupuję {sum(len(item) for item in lista_zakupow.values())} produktów")
print(3**3)