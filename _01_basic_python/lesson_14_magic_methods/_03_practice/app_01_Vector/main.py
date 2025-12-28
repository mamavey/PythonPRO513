from classes.ClassVector import Vector2D

if __name__ == '__main__':
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(v1 + v2)
    # print(v1 + "строка")
    print(v1 - v2)
    print(len(v1))
    print(f'Длина: {(v1 + v2).length():.2f}')
    print(f'Угол: {v1.angle():.2f}')