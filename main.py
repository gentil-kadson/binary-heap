from classes import BinaryHeap, BinaryItem

# 1ST DATASET
first_heap_dataset = BinaryHeap()

# 1.
first_heap_dataset.insert(BinaryItem(10))
first_heap_dataset.insert(BinaryItem(5))
first_heap_dataset.insert(BinaryItem(20))
first_heap_dataset.insert(BinaryItem(1))
first_heap_dataset.insert(BinaryItem(15))
first_heap_dataset.insert(BinaryItem(30))
first_heap_dataset.insert(BinaryItem(25))

# 2.
first_heap_dataset.change_priority(3, 50)
first_heap_dataset.change_priority(1, 8)

# 3.
first_heap_dataset.remove()
first_heap_dataset.remove()
first_heap_dataset.remove()

# 4.
first_heap_dataset.heap_sort()

# 5.
first_heap_dataset.get_high_priority()

# 2ND DATASET
second_heap_dataset = BinaryHeap()

# 1.
second_heap_dataset.insert(BinaryItem(1))
second_heap_dataset.insert(BinaryItem(2))
second_heap_dataset.insert(BinaryItem(3))
second_heap_dataset.insert(BinaryItem(4))
second_heap_dataset.insert(BinaryItem(5))
second_heap_dataset.insert(BinaryItem(6))
second_heap_dataset.insert(BinaryItem(7))
second_heap_dataset.insert(BinaryItem(8))
second_heap_dataset.insert(BinaryItem(9))
second_heap_dataset.insert(BinaryItem(10))

# 2.
second_heap_dataset.change_priority(4, 15)
second_heap_dataset.change_priority(8, 3)

# 3.
second_heap_dataset.remove()
second_heap_dataset.remove()
second_heap_dataset.remove()
second_heap_dataset.remove()
second_heap_dataset.remove()

# 4.
second_heap_dataset.heap_sort()

# 5.
second_heap_dataset.get_high_priority()
