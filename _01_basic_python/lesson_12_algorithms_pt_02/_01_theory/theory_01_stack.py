def push(stack, item):
    stack.append(item)


def pop(stack):
    if stack:
        item = stack.pop()
        return item
    return None

def peek(stack):
    if stack:
        print(stack[-1])
    else:
        print(f'Стек пуст!')


if __name__ == '__main__':
    my_stack = []
    push(my_stack, 'data_1')
    push(my_stack, 'data_2')
    push(my_stack, 'data_3')
    print(my_stack[::-1]) # для отображения!!!
    peek(my_stack)

    item_3 = pop(my_stack)
    item_2 = pop(my_stack)
    print(item_3)
    print(item_2)
    print(pop(my_stack))
    print(pop(my_stack))
    print(pop(my_stack))
    # stack = []
    # stack.append(1)
    # stack.append(2)
    # stack.append(3)
    # print(stack[::-1])  # для отображения!!!
    #
    # item3 = stack.pop()
    # print(item3)
    # print(stack[::-1])
    # print(stack[-1])
