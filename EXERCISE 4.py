def generate_right_triangle():
    height = int(input("Enter the height of the triangle: "))
    for i in range(height, 0, -1):
        print("*" * i)
generate_right_triangle()