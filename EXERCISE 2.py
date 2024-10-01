def generate_hollow_square():
    side_length = int(input("Enter the side length of the square: "))
    print("x" * side_length)
    for _ in range(side_length - 2):
        print("x" + " " * (side_length - 2) + "x")
    print("x" * side_length)
generate_hollow_square()