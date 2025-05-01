text=input ("Каалагандай текст киргизиниз! ")
symbol=input("Кайсыл тамганы издейли? ")
number=text.count(symbol)
if number==0:
    print("Мындай тамга тексте жок!")
else:
    print(f"Тексте {number} тамга '{symbol}'")

