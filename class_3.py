class Class:
    def __init__(self,n="Белый"):
        self.name=n;
        print("Создан объект:",self.name)

    def __del__(self):
        print("Удален объект:",self.name)

def create(n):
    obj=Class(n)

a=Class()
b=Class("Красный")
c=Class("Синий")

create("Желтый")
c.name="Зеленый"

del a
del b
del c
