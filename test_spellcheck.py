# # test_spellcheck.py 
# from curses.ascii import isdigit
import pytest
import spellcheck as sc
# ''' 
# Import statements: 
#     1. Import pytest and spellcheck modules
# '''
# ### WRITE IMPORT STATEMENTS HERE

# # String variables to be tested
# alpha = "Checking the length & structure of the sentence."
# beta = "This sentence should fail the test"

# # Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
# @pytest.fixture
# def input_value():
#     # Default input value for testing
#     input = alpha
#     return input

# # First test function test_length()
# def test_length(input_value):
#     assert sc.word_count(input_value) <10
#     assert sc.char_count(input_value) <50
#     """ 
#     Tests whether a string has fewer than 10 words and fewer than 50 chars.

#     [IMPLEMENT ME]
#         1. Use an assert statement to check the given string has fewer than 10 words
#         2. Use an assert statement to check the given string has fewer than 50 chars

#     Args:
#       input_value: a function that returns a string, which can be configured
#                    in the input_value() function
#     """
#     ### WRITE SOLUTION CODE HERE

# # Second test function test_struc()
# def test_struc(input_value):
#     assert sc.first_char(input_value).isupper()
#     assert sc.last_char(input_value) == '.'
    
    
    
#     """ 
#     Tests whether a string begins with a capital letter and ends with a period.

#     [IMPLEMENT ME]
#         1. Use an assert statement to check the given string begins with a capital letter
#         2. Use an assert statement to check the given string ends with a period ('.')

#     Args:
#       input_value: a function that returns a string, which can be configured
#                    in the input_value() function
#     """
#     ### WRITE SOLUTION CODE HERE

# # Run these tests with `python3 -m pytest test_spellcheck.py`


def test_nodigit():
    assert sc.nodigit("dcp")
    
# class A:
#    def a(self):
#        return "Function inside A"

# class B:
#    def a(self):
#        return "Function inside B"

# class C:
#    pass

# class D(C, A, B):
#    pass

# d = D()
# print(d.a())
def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()
def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)
    
num = 9
class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num = 11

cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
Car.num = 2
print(num)