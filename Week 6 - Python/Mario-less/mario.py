while True:
    try:
        height = int(input("Height (1-8): ")) 
        if 0 < height <= 8:
            break
    except ValueError:
        print("Please enter a number between (1-8)")

for i in range(height):
    # Print white spaces
    print(" " * (height - i - 1), end="")
    # Print hashes
    print("#" * (i + 1))




