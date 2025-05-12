from copy import *
class OurClass:
    pass
a=OurClass
a.value=100
a.nums=[1,2,3]
b=a
c=copy(a)
d=deepcopy(a)
print("Созданы объекты")
print("a:", a.value,"и",a.nums)
print("b:", b.value,"и",b.nums)
print("c:", c.value,"и",c.nums)
print("d:", d.value,"и",d.nums)
print("a.value=200 и a.nums[1]=0")
a.value=200
a.nums[1]=0

print("a:",a.value, "и", a.nums)
print("b:", b.value,"и", b.nums)
print("c:", c.value,"и", c.nums)
print("d:", d.value,"и", d.nums)
print("Удаляется а")

del a
print("b.value=300 и b.nums[2]=4")
b.value=300
b.nums[2]=4
print("b:", b.value,"и", b.nums)
print("c:", c.value,"и", c.nums)
print("d:", d.value,"и", d.nums)
