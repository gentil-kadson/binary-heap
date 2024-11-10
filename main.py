from classes import BinaryHeap, BinaryItem

game_1 = BinaryItem(4)
game_2 = BinaryItem(3)
game_3 = BinaryItem(2)
game_4 = BinaryItem(1)

array = [game_1, game_2, game_3, game_4]

my_heap = BinaryHeap(array)
my_heap.insert(BinaryItem(10))
print(my_heap)
my_heap.remove()
print(my_heap)
