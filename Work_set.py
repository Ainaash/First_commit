number=[5,1,60,23,7,89]
print("Тизме:",number)
print("Тизменин узундугу:",len(number))
print("Биринчи элемент:",number[0])
print("Акыркы элемент:",number[-1])
print("Эн чон элемент", max(number))
print("Эн кичине элемент", min(number))
print("Сумма:",sum(number))
print("Элементтерди тескерисинче чыгаруу:",list(reversed(number)))
print("Осуу мааниси",sorted(number))
print("Кемуу тартиби боюнча:",sorted(number,reverse=True))

