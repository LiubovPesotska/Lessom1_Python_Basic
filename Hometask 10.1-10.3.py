#Hometask 10.1
def some_gen(begin, end, func):
    """
    begin: first element of the sequence
    end: number of elements in the sequence
    func: function that defines the sequence values
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)
def pow(x):
    return x ** 2

gen = some_gen(2, 4, pow)

assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

#Hometask 10.2
import re

def first_word(text):
    """ Find the first word in the given text """
    match = re.search(r"[a-zA-Z']+", text)
    if match:
        return match.group(0)
    return ""

# Tests
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

#Hometask 10.3
def is_even(digit):
    """ Check if the number is even """
    return digit % 2 == 0

# Tests
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')