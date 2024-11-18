n = int(input("Введите необходимое количество элементов"))
numbers = []

for i in range(1, n+1):
    numbers += str(i) * i

print(" ".join(numbers[:n]))