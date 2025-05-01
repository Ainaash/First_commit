first = "\nСиз барган мамлекетти тандагыз:"
first += "\n(Чыгуу учун exit созун жазуу жетиштуу.) "

while True:
    country = input(first)

    if country == 'exit':
        break
    else:
        print("Мага жаккан мамлекет " + country.title() + "!")