
import math_series.math_series as series
import pytest


#######################################
# Fibonacci Tests
# Test 1
def test_Fibonacci():
    '''It should return [0,2]'''
    assert series.Fibonacci(0) == 0

# Test 2


def test_Fibonacci_test_One():
    ''' It should return [1,1] '''
    assert series.Fibonacci(1) == 1

# Test 3


def test_Fibonacci_test_five():
    '''It should return 5'''
    assert series.Fibonacci(5) == 5
# Test 4


def test_Fibonacci_test_ten():
    '''It should return 55'''
    assert series.Fibonacci(10) == 55

    #######################################
    # Lucas Tests
# Test 5


def test_lucas_test_Zero():
    '''It should return 2'''
    assert series.lucas(0), 2

# Test 6


def test_lucas_test_One():
    ''' It should return 1 '''
    assert series.lucas(1), 1

# Test 7


def test_lucas_test_five():
    '''It should return 11'''
    assert series.lucas(5), 11
# Test 8


def test_lucas_test_ten():
    '''It should return 123'''
    assert series.lucas(10), 123

    #######################################
    # Sum_Seris Tests

    #limit = 6
# Test 9


def test_Sum_Seris_test_first_number_1_second_number_0_limit_6():
    '''It should return 5'''
    assert series.sum_series(6, 1, 0), 8

# Test 10


def test_Sum_Seris_test_first_number_0_second_number_1_limit_6():
    ''' It should return 5 '''
    assert series.sum_series(6, 0, 1), 8

# Test 11


def test_Sum_Seris_test_first_number_2_second_number_1_limit_6():
    '''It should return 11'''
    assert series.sum_series(6, 2, 1), 18
# Test 12


def test_Sum_Seris_test_first_number_1_second_number_2_limit_6():
    '''It should return 11'''
    assert series.sum_series(6, 1, 2), 18
    #############    Sum_Seris Tests    ###############
    # limit = 10
# Test 13


def test_Sum_Seris_test_first_number_1_second_number_0_limit_10():
    '''It should return 5'''
    assert series.sum_series(10, 1, 0), 55
# Test 14


def test_Sum_Seris_test_first_number_0_second_number_1_limit_10():
    ''' It should return 5 '''
    assert series.sum_series(10, 0, 1), 55

# Test 15


def test_Sum_Seris_test_first_number_2_second_number_1_limit_10():
    '''It should return 11'''
    assert series.sum_series(10, 2, 1), 123
# Test 16


def test_Sum_Seris_test_first_number_1_second_number_2_limit_10():
    '''It should return 11'''
    assert series.sum_series(10, 1, 2), 123

    ###### Invaild inputs testing ######
# Test 17


def test_Sum_Seris_Invalid_num1_num2():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        5, -6, -3) == "Enter a vaild number(Not a string , not below 0)"
# Test 18


def test_Sum_Seris_Invalid_limit():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(-10, 5,
                             2) == "Enter a vaild number(Not a string , not below 0)"
# Test 19


def test_Sum_Seris_Invalid_Invalid_limit_and_num2():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(-5, 6, -
                             3) == "Enter a vaild number(Not a string , not below 0)"
# Test 20


def test_Sum_Seris_Invalid_Invalid_limit_and_num1():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(-5, -6,
                             3) == "Enter a vaild number(Not a string , not below 0)"
    #################


def test_Sum_Seris_Zero():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(0) == 0


def test_Sum_Seris_Onee():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(1) == 1


def test_Sum_Seris_Two():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(2) == 1


def test_Sum_Seris_ten():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(10) == 55


def test_Sum_Seris_Invalid_Invalid_limit_and_num1():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        "hi") == "Enter a vaild number(Not a string , not below 0)"

    #############


def test_Sum_Seris_first_input_string():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        "hi", 2, 3) == "Enter a vaild number(Not a string , not below 0)"
    #############


def test_Sum_Seris_sec_input_string():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        1, "hi", 2) == "Enter a vaild number(Not a string , not below 0)"
    #############


def test_Sum_Seris_third_input_string():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        2, 2, "hi") == "Enter a vaild number(Not a string , not below 0)"
    #############  ########


def test_Sum_Seris_first_input_Zero():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(0, 5, 8) == 5
    #############


def test_Sum_Seris_not_fib_not_lucas():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(1, 5, 8) == 8
    #####################


def test_Sum_Seris_not_fib_not_lucas_2():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(2, 5, 8) == 13


def test_Sum_Seris_not_fib_not_lucas_3():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(10, 5, 8) == 610


def test_Sum_Seris_first_input_negative():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(-1, 5,
                             8) == "Enter a vaild number(Not a string , not below 0)"


def test_Sum_Seris_first_input_string_lucas():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        "test", 2, 1) == "Enter a vaild number(Not a string , not below 0)"
    #########


def test_Sum_Seris_all_strings():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        "test", "test", "test") == "Enter a vaild number(Not a string , not below 0)"


def test_Sum_Seris_last_two_inputs_strings():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        2, "test", "test") == "Enter a vaild number(Not a string , not below 0)"


def test_Sum_Seris_first_two_inputs_strings():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.sum_series(
        "test", "test", 1) == "Enter a vaild number(Not a string , not below 0)"
# 3

# Test 21


def test_Fibonacci_Invalid_limit():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.Fibonacci(-2) == "Enter a vaild number(Not a string , not below 0)"
# Test 22


def test_lucas_Invalid_limit():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.lucas(-2) == "Enter a vaild number(Not a string , not below 0)"
# Test 23


def test_Fibonacci_Invalid_limit_String():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.Fibonacci(
        "test") == "Enter a vaild number(Not a string , not below 0)"
    # Test 24


def test_lucas_Invalid_limit_String():
    '''It should return Enter a vaild number(Not a string , not below 0)'''
    assert series.lucas(
        "test") == "Enter a vaild number(Not a string , not below 0)"
