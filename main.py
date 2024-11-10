from classes import BinaryHeap, BinaryItem

game_1 = BinaryItem(4)
game_2 = BinaryItem(3)
game_3 = BinaryItem(2)
game_4 = BinaryItem(1)

array = [game_1, game_2, game_3, game_4]

my_heap = BinaryHeap(array)
print(my_heap)

my_heap.insert(BinaryItem(10))
my_heap.get_high_priority()

my_heap.change_priority(4, 11)
my_heap.heap_sort(len(my_heap.get_array()) - 1)
print("eu juro você vai pagar")
print(my_heap)
