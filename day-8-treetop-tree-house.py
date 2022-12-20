
with open('day-8-input.txt', 'r') as f:

    data = tuple(tuple(int(n) for n in line.rstrip()) for line in f)

    width = len(data[0])
    height = len(data)
