import math


class BinaryItem:
    def __init__(self, value, key):
        self.__value = value
        self.__key = key

    def get_value(self):
        return self.__value

    def set_value(self, value) -> None:
        self.__value = value

    def get_key(self):
        return self.__key

    def set_key(self, key) -> None:
        self.__key = key


class BinaryHeap:
    def __init__(self, array: list[BinaryItem] = []):
        self.__array: list[BinaryItem] = [BinaryItem(math.inf, 0), *array]

    def get_array(self) -> list[BinaryItem]:
        return self.__array

    def go_up(self, index: int) -> None:
        parent_index = index // 2
        if parent_index >= 1:
            if self.__array[index].get_key() > self.__array[parent_index].get_key():
                aux = self.__array[parent_index]
                self.__array[parent_index] = self.__array[index]
                self.__array[index] = aux
                self.go_up(parent_index)

    def go_down(self, index: int, n_of_existing_elements: int) -> None:
        child_index = 2 * index

        if child_index <= n_of_existing_elements:
            if child_index < n_of_existing_elements:
                if self.__array[child_index+1].get_key() > self.__array[child_index].get_key():
                    child_index += 1
            if self.__array[index].get_key() < self.__array[child_index].get_key():
                aux = self.__array[child_index]
                self.__array[child_index] = self.__array[index]
                self.__array[index] = aux
                self.go_down(child_index, n_of_existing_elements)

    def __str__(self):
        array_data = [
            f"{item.get_value()}, {item.get_key()}" for item in self.__array[1:]]
        return "\n".join(array_data)
