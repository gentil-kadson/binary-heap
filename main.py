from classes import BinaryHeap, BinaryItem

game_1 = BinaryItem("Dark Souls", 4)
game_2 = BinaryItem("Bloodborne", 2)
game_3 = BinaryItem("Elden Ring", 1)
game_4 = BinaryItem("Sekiro", 3)

array = [game_1, game_2, game_3, game_4]

my_heap = BinaryHeap(array)
