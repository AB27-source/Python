from math import factorial

# function find max number of three given numbers
def max_num(num1, num2, num3):
    return max([num1,num2,num3])

# function multiplies numbers in list
def mult_list(list):
    # checks if list is empty
    if len(list) == 0:
        return 0
    
    # returns first element if list len = 1
    if len(list) == 1:
        return list[0]
    
    # setting result = first element
    result = list[0]

    # looping through list and multiplying result with index i
    for i in list[1:]:
        result = result * i
    
    # returning result
    return result

# function reverses string
def rev_string(str):
    return str[::-1]


# function checks if number is within range
def num_within(num, start, end):
    return num in range(start, end+1)

# Pascals Triangle Function
def pascal(num):
    # checks if num is less than 1
    if num < 1:
        print ("num cannont be less than 1")
    
    for i in range(num+1):
        total = 1
        for j in range (1, i+1):
            print(total," ", end="")
            total = total * (i - j) // j
        print()
    return ""



# outputs
print(max_num(2,412,213))

list1 = [1, 2, 3]
print(mult_list(list1))

print(rev_string("Hello World!"))

print(num_within(5,1,10))
print(num_within(21,1,10))

print(pascal(5))