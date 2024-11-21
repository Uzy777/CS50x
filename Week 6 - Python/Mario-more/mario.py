while True:
    try:
        height = int(input("Height (1-8): ")) 
        if 0 < height <= 8:
            break
    except ValueError:
        print("Please enter a number between (1-8)")

for i in range(height):
    # Print white spaces for the left pyramid
    print(" " * (height - i - 1), end="")
    # Print the left pyramid
    print("#" * (i + 1), end="")
    # Print fixed gap between pyramids
    print("  ", end="")
    # Print the right pyramid
    print("#" * (i + 1))
    





