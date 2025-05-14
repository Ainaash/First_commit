# Написать класс который, имеет поле array
# и реализует инкапсуляцию по отношению array,
# так чтобы она не оставалось пустым
# и не присваивалось туда дублирующиеся значения
#
# Написать набор классов,
# которые реализуют методы:
#  - get() - получает последний элемент из массива - array
#  - update() - обновляет последний элемент из массива - array
#  - pop() - удаляет последний элемент из массива - array
# """

class WorkWithArray:
    def init(self, array):
        self._array = array

    @property
    def get_array(self):
        return self._array

    @get_array.setter
    def get_array(self, value):
        ...

class GetArray(WorkWithArray):
    def init(self, array):
        super().init(array)

    def get(self):
        return self._array[-1]

get_arr=GetArray([1,2,3])
result = get_arr.get()
print(result)