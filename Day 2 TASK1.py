y = []
x = int(input("enter the no. of elements: "))
print("enter the elements:")
for i in range(x):
    num = int(input(f"element {i+1}: "))
    y.append(num)

ascendig = sorted(y)
print("ascending order:", ascendig)

descending = sorted(y, reverse=True)
print("descending order:", descending)