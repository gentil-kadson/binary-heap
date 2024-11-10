from classes import BinaryHeap, BinaryItem


def first_dataset() -> None:
    # 1ST DATASET
    print("========1ST DATASET========")
    items = [BinaryItem(10),
             BinaryItem(5),
             BinaryItem(20),
             BinaryItem(1),
             BinaryItem(15),
             BinaryItem(30),
             BinaryItem(25)]
    first_heap_dataset = BinaryHeap()

    # 1.
    print("1. HEAP CONSTRUCTION")
    for item in items:
        first_heap_dataset.insert(item)

    # 2.
    print("\n2. PRIORITY CHANGE")
    first_heap_dataset.change_priority(3, 50)
    first_heap_dataset.change_priority(1, 8)

    # 3.
    print("\n3. REMOVALS")
    for _ in range(3):
        first_heap_dataset.remove()

    # 4.
    print("\n4. HEAPSORT FUNCTION")
    first_heap_dataset.heap_sort()

    # 5.
    print("\n5. HIGH PRIORITY NODE")
    first_heap_dataset.get_high_priority()


def second_dataset() -> None:
    # 2ND DATASET
    print("\n========2ND DATASET========")
    items = [BinaryItem(1),
             BinaryItem(2),
             BinaryItem(3),
             BinaryItem(4),
             BinaryItem(5),
             BinaryItem(6),
             BinaryItem(7),
             BinaryItem(8),
             BinaryItem(9),
             BinaryItem(10)]
    second_heap_dataset = BinaryHeap()

    # 1.
    print("1. HEAP CONSTRUCTION")
    for item in items:
        second_heap_dataset.insert(item)

    # 2.
    print("\n2. PRIORITY CHANGE")
    second_heap_dataset.change_priority(4, 15)
    second_heap_dataset.change_priority(8, 3)

    # 3.
    print("\n3. REMOVALS")
    for _ in range(5):
        second_heap_dataset.remove()

    # 4.
    print("\n4. HEAPSORT FUNCTION")
    second_heap_dataset.heap_sort()

    # 5.
    print("\n5. HIGH PRIORITY NODE")
    second_heap_dataset.get_high_priority()


def third_dataset() -> None:
    # 3RD DATASET
    print("\n========3RD DATASET========")
    items = [BinaryItem(50),
             BinaryItem(40),
             BinaryItem(30),
             BinaryItem(20),
             BinaryItem(10),
             BinaryItem(5),
             BinaryItem(3)]
    third_heap_dataset = BinaryHeap()

    # 1.
    print("1. HEAP CONSTRUCTION")
    for item in items:
        third_heap_dataset.insert(item)

    # 2.
    print("\n2. PRIORITY CHANGE")
    third_heap_dataset.change_priority(2, 60)
    third_heap_dataset.change_priority(5, 1)

    # 3.
    print("\n3. REMOVALS")
    for _ in range(3):
        third_heap_dataset.remove()

    # 4.
    print("\n4. HEAPSORT FUNCTION")
    third_heap_dataset.heap_sort()

    # 5.
    print("\n5. HIGH PRIORITY NODE")
    third_heap_dataset.get_high_priority()


def fourth_dataset() -> None:
    # 4TH DATASET
    print("\n========4TH DATASET========")
    items = [BinaryItem(13),
             BinaryItem(26),
             BinaryItem(19),
             BinaryItem(17),
             BinaryItem(24),
             BinaryItem(31),
             BinaryItem(22),
             BinaryItem(11),
             BinaryItem(8),
             BinaryItem(20),
             BinaryItem(5),
             BinaryItem(27),
             BinaryItem(18)]
    fourth_heap_dataset = BinaryHeap()

    # 1.
    print("1. HEAP CONSTRUCTION")
    for item in items:
        fourth_heap_dataset.insert(item)

    # 2.
    print("\n2. PRIORITY CHANGE")
    fourth_heap_dataset.change_priority(7, 35)
    fourth_heap_dataset.change_priority(10, 12)

    # 3.
    print("\n3. REMOVALS")
    for _ in range(4):
        fourth_heap_dataset.remove()

    # 4.
    print("\n4. HEAPSORT FUNCTION")
    fourth_heap_dataset.heap_sort()

    # 5.
    print("\n5. HIGH PRIORITY NODE")
    fourth_heap_dataset.get_high_priority()

    print("\n========END OF EXECUTION========")
