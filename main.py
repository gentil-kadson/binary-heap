from classes import BinaryHeap, BinaryItem

# # 1ST DATASET
# first_heap_dataset = BinaryHeap()

# # 1.
# first_heap_dataset.insert(BinaryItem(10))
# first_heap_dataset.insert(BinaryItem(5))
# first_heap_dataset.insert(BinaryItem(20))
# first_heap_dataset.insert(BinaryItem(1))
# first_heap_dataset.insert(BinaryItem(15))
# first_heap_dataset.insert(BinaryItem(30))
# first_heap_dataset.insert(BinaryItem(25))

# # 2.
# first_heap_dataset.change_priority(3, 50)
# first_heap_dataset.change_priority(1, 8)

# # 3.
# first_heap_dataset.remove()
# first_heap_dataset.remove()
# first_heap_dataset.remove()

# # 4.
# first_heap_dataset.heap_sort()

# # 5.
# first_heap_dataset.get_high_priority()

# # 2ND DATASET
# second_heap_dataset = BinaryHeap()

# # 1.
# second_heap_dataset.insert(BinaryItem(1))
# second_heap_dataset.insert(BinaryItem(2))
# second_heap_dataset.insert(BinaryItem(3))
# second_heap_dataset.insert(BinaryItem(4))
# second_heap_dataset.insert(BinaryItem(5))
# second_heap_dataset.insert(BinaryItem(6))
# second_heap_dataset.insert(BinaryItem(7))
# second_heap_dataset.insert(BinaryItem(8))
# second_heap_dataset.insert(BinaryItem(9))
# second_heap_dataset.insert(BinaryItem(10))

# # 2.
# second_heap_dataset.change_priority(4, 15)
# second_heap_dataset.change_priority(8, 3)

# # 3.
# second_heap_dataset.remove()
# second_heap_dataset.remove()
# second_heap_dataset.remove()
# second_heap_dataset.remove()
# second_heap_dataset.remove()

# # 4.
# second_heap_dataset.heap_sort()

# # 5.
# second_heap_dataset.get_high_priority()

# # 3RD DATASET
# third_heap_dataset = BinaryHeap()

# # 1.
# third_heap_dataset.insert(BinaryItem(50))
# third_heap_dataset.insert(BinaryItem(40))
# third_heap_dataset.insert(BinaryItem(30))
# third_heap_dataset.insert(BinaryItem(20))
# third_heap_dataset.insert(BinaryItem(10))
# third_heap_dataset.insert(BinaryItem(5))
# third_heap_dataset.insert(BinaryItem(3))

# # 2.
# third_heap_dataset.change_priority(2, 60)
# third_heap_dataset.change_priority(5, 1)

# # 3.
# third_heap_dataset.remove()
# third_heap_dataset.remove()
# third_heap_dataset.remove()

# # 4.
# third_heap_dataset.display_heap()
# third_heap_dataset.heap_sort()

# # 5.
# third_heap_dataset.get_high_priority()

# 4TH DATASET
items = [BinaryItem(13), BinaryItem(26), BinaryItem(19), BinaryItem(17), BinaryItem(
    24), BinaryItem(31), BinaryItem(22), BinaryItem(11), BinaryItem(8), BinaryItem(20), BinaryItem(5), BinaryItem(27), BinaryItem(18)]
fourth_heap_dataset = BinaryHeap()

# 1.
for item in items:
    fourth_heap_dataset.insert(item)

# 2.
fourth_heap_dataset.change_priority(7, 35)
fourth_heap_dataset.change_priority(10, 12)

# 3.
for _ in range(4):
    fourth_heap_dataset.remove()

# 4.
fourth_heap_dataset.heap_sort()

# 5.
fourth_heap_dataset.get_high_priority()
