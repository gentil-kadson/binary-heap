import math


class BinaryItem:
    def __init__(self, value, key=None):
        self.__value = value
        self.__key = value if key is None else key

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

    def display_heap(self) -> None:
        print(self)

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

    def insert(self, new_item: BinaryItem) -> None:
        self.__array.append(new_item)
        self.go_up(len(self.__array) - 1)
        self.display_heap()

    def remove(self) -> None:
        aux = self.__array[1]
        self.__array[1] = self.__array[-1]
        self.__array[-1] = aux
        self.__array.pop()
        self.go_down(1, len(self.__array) - 1)
        self.display_heap()

    def get_high_priority(self):
        print(self.__array[1].get_value())

    def arrange(self, n_of_existing_elements: int) -> None:
        for i in range(n_of_existing_elements // 2, 0, -1):
            self.go_down(i, n_of_existing_elements)

    def heap_sort(self, n_of_existing_elements: int) -> None:
        self.arrange(n_of_existing_elements)
        aux = n_of_existing_elements
        while aux > 1:
            swap_aux = self.__array[1]
            self.__array[1] = self.__array[aux]
            self.__array[aux] = swap_aux
            aux -= 1
            self.go_down(1, aux)
            self.display_heap()

    def change_priority(self, index: int, new_priority_key) -> None:
        self.__array[index].set_key(new_priority_key)
        self.__array[index].set_value(new_priority_key)
        self.arrange(len(self.__array) - 1)
        self.display_heap()

    def __str__(self) -> str:
        array_data = [
            item.get_value() for item in self.__array[1:]]
        return f"{array_data}"
