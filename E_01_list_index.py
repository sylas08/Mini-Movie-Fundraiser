import random

fruit_list = ['apple', 'banana', 'cherry', 'dragon fruit']
colour_list = ['green', 'yellow', 'red', 'pink']

first_fruit = random.choice(fruit_list)

# find the position of the selected time
fruit_index = fruit_list.index(first_fruit)

first_colour = colour_list[fruit_index]

print(f"first fruit: {first_fruit} | first colour: {first_colour}")

