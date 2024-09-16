def countSteps(x, y):
    if x < y:
        return x + y + 2 * ((y - x) // 2)

    else:
        return x + y + 2 * (((x - y) + 1) // 2)

if __name__ == "__main__":
    x, y = 4, 3
    print(countSteps(x, y))
