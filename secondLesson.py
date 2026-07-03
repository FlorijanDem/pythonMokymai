import calendar

def sum_of_list(array):
    sum = 0
    for i in array:
        sum = sum + i

    return sum
print("2 uzduotis")
print(sum_of_list([4,3,7]))

def biggest_number(*args):
    if len(args) == 0:
        return None
    biggest = args[0]
    for i in args:
        if biggest < i:
            biggest = i
    return biggest


print("3 uzduotis")
print(biggest_number(34, 111, 23, 65))

def reverse_string(text):
    x = text[::-1]
    return x


print("4 uzduotis")
print(reverse_string("hello"))

def type_finder(text):
    wordsSplited = text.split()
    words = len(wordsSplited)

    upperCases = 0
    lowerCases = 0
    numbers = 0

    for i in text:
        if i.isupper():
            upperCases = upperCases + 1
        if i.islower():
            lowerCases = lowerCases + 1

        if i.isnumeric():
            numbers = numbers + 1

    result = f"Words: {words} Upper: {upperCases} Lower {lowerCases} Numbers {numbers}"
    return result
print("5 uzduotis")
print(type_finder("Welcome to 1St birsday"))

def out_only_unicue(data):
    result = list(set(data))
    return result

print("6 uzduotis")
print(out_only_unicue(["As", "As"]))

def prime_numbers(number):
    if (number <=1):
        return False
    else:
        try:
            for i in range(2, int(number**0.5) + 1):
                if number %i == 0:
                    return False
        except:
            print("Something going wrong")
        else:
            return True
    
print("7 uzduotis")
print(prime_numbers(11))

def sort_string(text):
    return "".join(sorted(text))

print("8 uzduotis")
print(sort_string("hello"))

def leap_year(year):
    if (calendar.isleap(year)):
        return True
    else:
        return False
    
print("9 uzduotis")
print(leap_year(2026))