import sys


def beautifulTriplets(d, arr):
    res = 0

    for el in arr:
        if el + d in arr and el + 2 * d in arr:
            res += 1

    return res


if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)

    # --------------------------------------------------------------------
    def beautifulTriplets(d, arr):
        a = set(arr)
        return len([1 for i in arr if i + d in a and i + d * 2 in a])


    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(beautifulTriplets(d, arr))