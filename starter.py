# print("Hello World")
# print_name("JeddyHwang")

# def print_name(name):
#     print(name)


# first_name = "Lorin"
# last_name = "Knudson"

# age = 41
# age = 15

# age = "forty-one"
# print(age)

# if age >= 18:
#     print("I am an adult")
# elif age < 13:
#     print("I am an infant")
# else:
#     print("I am an Alien Spock")

#     print("Goodbye World")

# print_name(first_name)
# print_name(last_name)

# print(first_name, last_name)

# favorite_numbers = [1, 2, 3, 4, 5, "hello", True, 2.0]
# print(favorite_numbers)

# for garbage in favorite_numbers:
#     print(garbage)

# for stuff in range(5):
#     print(stuff)

# x = 1
# y = 2

# def sum(x, y):
#     print(x + y)

# sum(x, y)

# num_1 = 1
# num_2 = 2

# def sum(num_1, num_2):
#     return num_1 + num_2

# result = sum(2, 3)

# print(result)

# print(sum(1, 2))


open_file = open("FinalGrades.csv")

# print(open_file)

# Counter Variables.
total_a = 0  
total_b = 0
total_c = 0

for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values)
    for value in values: 
        if value == "A":
            total_a +=1
        elif value == "B":
            total_b +=1
        elif value == "C":
            total_c +=1


print("A's:", total_a)
print("B's:", total_b)
print("Cs:", total_c)

open_file.seek(0)
# open_file = open("FinalGrades.csv")

for line in open_file:
    line = line.strip()
    values = line.split(",")
    print(values[2: 5])

open_file.close()
        