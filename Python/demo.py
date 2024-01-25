# Call from command line: python demo.py

def hello():
    print("Hello, world!")

def add_numbers(a, b):
    return a + b

# create a list of 7 three digit random numbers
import random
def create_random_list():
    random_list = []
    for i in range(7):
        random_list.append(random.randint(100, 999))
    return random_list

random_list = create_random_list()

# Create a function to find out how many numbers are larger than the previous number in a list
def find_larger_than_previous(random_list):
    count = 0
    for i in range(len(random_list) - 1):
        if random_list[i+1] > random_list[i]:
            count += 1
    return count

def better_find_larger_than_previous(random_list):
    return sum(1 for x, y in zip(random_list, random_list[1:]) if y - x > 0)

# Call the function from the command line
if __name__ == "__main__":
    hello()
    # pass arguments from the command line
    import sys
    print(add_numbers(int(sys.argv[1]), int(sys.argv[2])))
    # python demo.py 3 4

    random_list = create_random_list()



# Path: Python/demo.py













