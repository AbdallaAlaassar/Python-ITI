
def mario_pyramid(height):
    for i in range(1, height + 1):
        
        print(" " * (height - i) + "*" * i)
