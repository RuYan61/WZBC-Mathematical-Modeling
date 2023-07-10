num = 3
boat_limit = 2

D = []
for u in range(0, boat_limit + 1):
    for v in range(0, boat_limit + 1):
        if 1 <= u + v <= boat_limit:
            D.append((u, v))

print(D)