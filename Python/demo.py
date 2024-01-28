# import sys module to read command line arguments
import sys

# Create a function to print hello world
def hello_world():
    print("Hello World")

# Create a function which accepts two integers and returns their sum
def add_two_numbers(a, b):
    return a + b

# Create a function to generate a list of 7 3 digit random numbers.
def generate_random_numbers():
    import random
    random_numbers = []
    for i in range(7):
        random_numbers.append(random.randint(100, 999))
    return random_numbers

#  Create a function to find out how many numbers in the list are larger than the previous number and return the count.
def count_larger_numbers(numbers):
    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            count += 1
    return count

def better_count_larger_numbers(numbers):
    return sum(1 for x, y in zip(numbers, numbers[1:]) if y > x)

# Create a function to get the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Create a function to call hello_world function from command line
if __name__ == "__main__":
    hello_world()
    # pass two integers from command line and add them
    print(add_two_numbers(int(sys.argv[1]), int(sys.argv[2])))
    # generate random numbers
    random_numbers = generate_random_numbers()
    print(random_numbers)
    # count larger numbers
    print(count_larger_numbers(random_numbers))
    # better count larger numbers
    print(better_count_larger_numbers(random_numbers))

















