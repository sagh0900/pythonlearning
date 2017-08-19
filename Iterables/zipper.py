sunday = [10, 22, 34, 51]
monday = [22, 35, 41, 47]
for item in zip(sunday, monday):
    print(item)
for sun, mon in zip(sunday, monday):
    print("average =", (sun + mon) / 2)

