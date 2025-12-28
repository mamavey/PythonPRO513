from collections import deque


def enqueue(queue: deque, item):
    queue.append(item)


def dequeue(queue: deque):
    if queue:
        item = queue.popleft()
        return item
    return None


if __name__ == '__main__':
    my_queue = deque()
    enqueue(my_queue, 'item_01')
    enqueue(my_queue, 'item_02')
    enqueue(my_queue, 'item_03')
    print(my_queue)

    print(dequeue(my_queue))
    print(dequeue(my_queue))
    print(dequeue(my_queue))
    print(dequeue(my_queue))

# queue = deque()
# print(queue)
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
#
# print(queue.popleft())
# print(queue.popleft())
# print(queue)
