import time
import matplotlib.pyplot as plt

# takes the Grid by the format of UxU
grid_num = list(map(lambda x: int(x), input("Input a grid by pixels example(\"4x4\") :").split("x")))

# Just for testing an Initial Model
init_state = [[0,1,0],[0,0,1],[1,1,1]]

def show(items):
    for i in items:
        print(i)
    print("\n")

def grid_sizer(size,matrix):
    if 1 == any(matrix[0]):
      matrix.insert(0,[0 for i in range(size[0])])
      matrix.append([0 for i in range(size[0])])
      for row in matrix:
          row.insert(0,0)
          row.append(0)
      size[0]+=2
      size[1]+=2
    elif 1 == any(matrix[size[0]-1]):
        matrix.insert(0,[0 for i in range(size[0])])
        matrix.append([0 for i in range(size[0])])
        for row in matrix:
            row.insert(0,0)
            row.append(0)
        size[0]+=2
        size[1]+=2
    elif 1 == any([1 if 1 == any([matrix[i][0] for i in range(size[0])]) else 0]) or 1 == any([1 if 1 == any([matrix[i][-1] for i in range(size[0])]) else 0]):
        matrix.insert(0,[0 for i in range(size[0])])
        matrix.append([0 for i in range(size[0])])
        for row in matrix:
            row.insert(0,0)
            row.append(0)
        size[0]+=2
        size[1]+=2

# Function to display the grid
def display_grid(grid):
    plt.imshow(grid, cmap='binary')
    plt.draw()
    plt.pause(0.1)

# Checks if the next or the one before the original pixel exist nor it returns 0
def next_or_before(lst, index1, index2):
    element = 0
    try:
        if index1 >= 0:
            if index2 >= 0:
                element = lst[index1][index2]
                return element
        else:
            element = 0
            return element
    except IndexError:
        element = 0
        return element
    return element

counter = 0
generation = 0
for line in init_state:
    print(line)
print("\n")

# Set interactive mode on
plt.ion()

# Create a figure to display the grid
fig = plt.figure()


buffer = []

# Counts the surrounding 8 pixels to apply rules to the pixel
# iterates through each pixel on the grid

while True:
    grid_sizer(grid_num, init_state)
    for x in list(range(0, grid_num[0])):
        buffer.insert(x, [])
        for y in list(range(0, grid_num[1])):
            var = 0
            counter = next_or_before(init_state, x, y + 1) + next_or_before(init_state, x, y - 1) + next_or_before(
                init_state, x - 1, y) + next_or_before(init_state, x - 1, y + 1) + next_or_before(init_state, x - 1,
                                                                                                  y - 1) + next_or_before(
                init_state, x + 1, y) + next_or_before(init_state, x + 1, y + 1) + next_or_before(init_state, x + 1,
                                                                                                  y - 1)

            if init_state[x][y] == 0:
                if counter >= 4:
                    var = 0
                elif counter == 3:
                    var = 1
                else:
                    var = 0
            elif init_state[x][y] == 1:
                if counter == 2:
                    var = 1
                elif counter == 3:
                    var = 1
                elif counter >= 4:
                    var = 0
                else:
                    var = 0
            else:
                pass
            buffer[x].insert(y,var)

            counter = 0
    grid_sizer(grid_num, buffer)
    show(init_state)
    display_grid(init_state)
    time.sleep(1)
    init_state = buffer
    buffer = []
    generation+=1
    print(generation)



# Turn off interactive mode
plt.ioff()
plt.show()
