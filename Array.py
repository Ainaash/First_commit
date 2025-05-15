class WorkWithArray:
    def __init__(self, array):

        self._array = array

    @property
    def get_array(self):
        return self._array

    @get_array.setter
    def get_array(self, value):
        if not value:
            raise ValueError("Array бош болбошу керек.")
        if len(set(value)) != len(value):
            raise ValueError("Кайталанган маанилерге тыюу салынат.")
        self._array = value

class GetArray(WorkWithArray):
    def __init__(self, array):
        super().__init__(array)

    def get(self):
        return self._array[-1]

    def update(self, new_value):
        if new_value in self._array:
            raise ValueError("Бул маани массивде буга чейин бар.")
        self._array[-1] = new_value

    def pop(self):
        return self._array.pop()


get_arr = GetArray([1, 2, 3])
result = get_arr.get()
print(result)


get_arr = GetArray([10, 20, 30])
print("Акыркы элемент:", get_arr.get())

get_arr.update(40)
print("Жаңыртылгандан кийин:", get_arr.get_array)

get_arr.pop()
print("pop() колдонгондон кийин:", get_arr.get_array)
