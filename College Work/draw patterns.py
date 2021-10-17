def draw_square(size):
    for count in range(size):
        print("X"*size)

def draw_rectangle(width, height):
    for count in range(height):
        print("X"*width)

def draw_rt_triangle_left(diagonal):
   for count in range (diagonal):
     print ("^"*count)

def draw_rt_triangle_right(diagonal):
    for count in range (diagonal):
      print (" "(diagonal-count)+"^"*count)

def draw_diamond (width):
    n = 0
    for i in range(1, width + 1):
        # loop to print spaces
        for j in range (1, (width - i) + 1):
            print(end = " ")
            
        # loop to print star
        while n != (2 * i - 1):
            print("#", end = "")
            n = n + 1
        n = 0
            
        # line break
        print()

    k = 1
    n = 1
    for i in range(1, width):
        # loop to print spaces
        for j in range (1, k + 1):
            print(end = " ")
        k = k + 1
            
        # loop to print star
        while n <= (2 * (width - i) - 1):
            print("#", end = "")
            n = n + 1
        n = 1
        print()

def print_menu():
    print()
    print("Please select from the following shapes:")
    print("1– Square")
    print("2– Rectangle")
    print("3– Right Triangle (left)")
    print("4– Right Triangle (right)")
    print("5– Diamond")
    print("0- Exit")

def get_dimension(dimension, shape):
    size = int(input("Please enter the "+dimension+" of the "+shape+": "))
    while size <= 0:
        print("Invalid size >>"+str(size)+"<<. Please enter a positive value.")
        size = int(input("Please enter the "+dimension+" of the "+shape+": "))
    return size

def ask_selection():
    selection = int(input("Please enter your selection: "))
    while selection < 0 or selection > 5:
        print("Invalid selection >>"+str(selection)+"<<.")
        selection = int(input("Please enter your selection: "))
    return selection

while True:
    print_menu()
    selection = ask_selection()
    # make a choice and call a function to print a shape
    if selection == 1:
        size = get_dimension("size", "square")
        draw_square(size)
    elif selection == 2:
        width = get_dimension("width", "rectangle")
        height = get_dimension("height", "rectangle")
        draw_rectangle(width,height)
    elif selection == 3:
        diagonal = get_dimension("diagonal", "right triangle (left)") + 1
        draw_rt_triangle_left(diagonal)
    elif selection == 4:
        diagonal = get_dimension("width", "diamond") + 1
        draw_rt_triangle_right(diagonal)
    elif selection == 5:
        width = get_dimension("width", "diamond")
        draw_diamond(width)
    elif selection == 0:
        break