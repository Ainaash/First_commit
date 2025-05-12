class MyClass:
    def set(self,n):
        self.number=n

    def show(self):
        print("Поле number=",self.number)
a=MyClass()
b=MyClass()
a.set(100)
b.set(200)
a.show()
b.show()
a.number=123
b.number=321
a.show()
b.show()