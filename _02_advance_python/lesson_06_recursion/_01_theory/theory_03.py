def count_workers_rec(sp):
    res = 0
    for item in sp:
        if isinstance(item, int):
            res += item
        else:
            res += count_workers_rec(item)
    return res


"""
1) 0 + 18 + count_workers_rec([[20, [10, 7]], 15])
2) 0 + 18 + count_workers_rec([20, [10, 7]]) / 15
3) 0 + 18 + count_workers_rec(20) / [10, 7] / 15
4) 0 + 18 + 20 + count_workers_rec([10, 7]) / 15
5) 0 + 18 + 20 + count_workers_rec(10))/ 7 / 15
6) 0 + 18 + 20 + 10 + count_workers_rec(7) / 15
7) 0 + 18 + 20 + 10 + 7 + count_workers_rec(15)
8) 0 + 18 + 20 + 10 + 7 + 15
"""

if __name__ == '__main__':
    count_Angola = 18
    count_New_York = [20, [10, 7]]
    count_Chicago = 15
    count_USA = [count_New_York, count_Chicago]
    # print(count_USA)
    count_all = [count_Angola, count_USA]
    print(count_all)
    print(count_workers_rec(count_all))
