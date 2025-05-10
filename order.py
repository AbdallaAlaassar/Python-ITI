
def sort_elements():
    y = []
    x = int(input("Enter the number of elements: "))
    print("Enter the elements:")
    for i in range(x):
        num = int(input(f"Element {i + 1}: "))
        y.append(num)

    ascending = sorted(y)
    print("Ascending order:", ascending)

    descending = sorted(y, reverse=True)
    print("Descending order:", descending)
