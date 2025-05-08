rows = int(input("Enter the number of rows: "))

pyramid = []

for i in range(1, rows + 1):
    line = "*" * i
    pyramid.append(line)

for line in pyramid:
    print(line)
