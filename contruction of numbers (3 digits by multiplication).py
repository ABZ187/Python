for a in range(1, 10):
    for b in range(1, 10):
        for d in range(1, 10):
            if a * b * d < 1000:
                c = str(a) + str(b) + str(d)
                c = int(c)
                # print(c, a * b)
                if c == a * b * d:
                    print("a is ", a, "b is ", b)
