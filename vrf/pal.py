# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
""" 
The structure of the algorithm is as follow:
    1. Create a list of all the numbers that we need to multiply i.e for three
       digit number [100, 101,  ...  , 999]
    2. Filter the list from the unwanted number, who can't create palindromic
       number, e.g 100, 110, 120, ...
    3. Run a for loop on the list to create the wanted multiplication, make
       some more filtration and check if the result is a palindromic number.
    4. Return the maximum.
"""


def max_palindrome(dig):
    """
    The function gets the wanted number of digits that the numbers to be
    multiplied should have, e.g dig=3 means that we will multiply the numbers
    from the following list [100, 101,  ...  , 999].
    The function returns the maximum palindromic number that can be created
    that way with the two values that created it.
    dig is the number of digit that the two multiplied numbers should have.
    """

    # This is the initialization of the wanted results
    max_pal = 0
    pal_value1 = 0
    pal_value2 = 0

    # Create a list of all the numbers that we need to multiply
    unfiltered_list = create_list(dig)

    # Filter the list from the unwanted number
    filtered_list = pal_filter(unfiltered_list)

    count = 0
    j = 0
    length_filtered = len(filtered_list)
    # Run a for loop on the list to create the wanted multiplication table
    # The use of i,j, count is in order to traverse only through half of the
    # multiplication table sliced through the diagonal
    while j < length_filtered:
        i = 0
        i = i + count
        while i < length_filtered:
            # filtration for numbers of the sort @@5*@@2
            if (filtered_list[j] % 5 == 0 & filtered_list[i] % 2 == 0) | \
                    (filtered_list[j] % 2 == 0 & filtered_list[i] % 5 == 0):
                i += 1
                continue
            else:
                result_multiplication = filtered_list[j]*filtered_list[i]
                if check_pal(result_multiplication):
                    # find the two 3-digit numbers that creates the max
                    if result_multiplication > max_pal:
                        pal_value1 = filtered_list[j]
                        pal_value2 = filtered_list[i]
                    max_pal = max(result_multiplication, max_pal)
            i += 1
        j += 1
        count += 1

    return max_pal, pal_value1, pal_value2


def create_list(dig):
    """
    The function gets the wanted number of digits that the numbers to be
    multiplied should have, e.g dig=3 means that we will multiply the numbers
    from the following list [100, 101,  ...  , 999].
    The function returns the list to be used in descending order i.e
    [999, 998, 997, ...,100].
    """
    max_range = pow(10, dig) - 1
    min_range = pow(10, dig-1) - 1
    unfiltered_list = list(range(max_range, min_range, -1))
    return unfiltered_list


def pal_filter(unfiltered_list):
    """
    The function gets a list, e.g. [100, 101,  ...  , 999].
    The function returns the filtered list without numbers that can be divided
    by 10, since they can't create palindromic number.
    """
    filtered_list = [x for x in unfiltered_list if (x % 10 != 0)]
    return filtered_list


def check_pal(number):
    """
    The function gets a number, convert it to str, travers through it and
    returns True if it's a palindromic else it returns False.
    """
    number_to_str = str(number)
    number_len = len(number_to_str)

    if number_len == 1:
        return True
    # If the length of the number is even
    elif number_len % 2 == 0:
        half_len = int(number_len / 2)
        for k in range(half_len):
            if (number_to_str[k] != number_to_str[-k - 1]):
                return False
        return True
    # If the length of the number is odd
    else:
        half_len = int((number_len - 1) / 2)
        for k in range(half_len):
            if (number_to_str[k] != number_to_str[-k - 1]):
                return False
        return True


print(max_palindrome(3))




