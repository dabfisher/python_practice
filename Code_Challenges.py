# 1 Control Flow

## 1.1. Large Power
import re
from this import d
from turtle import up


def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        return False
print('1.1')
print(large_power(2, 2))
print(large_power(2, 2000))

## 1.2. Over Budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    spent = food_bill + electricity_bill + internet_bill + rent
    if spent > budget:
        return True
    else:
        return False
print('1.2')
print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 40))

## 1.3. Twice As Large
def twice_as_large(num1, num2):
    num2_twice = num2*2
    if num2_twice == num1:
        return True
    else:
        return False
print('1.3')
print(twice_as_large(10, 5))
print(twice_as_large(11, 5))
print(twice_as_large(9, 5))

## 1.4. Divisible By Ten
def divisible_by_ten(num):
    if (num % 10 == 0):
        return True
    else:
        return False
print('1.4')
print(divisible_by_ten(100))
print(divisible_by_ten(101))

## 1.5. Not Sum To Ten
def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False
print('1.5')
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(9, -1))

# 2 Control Flow (Advanced)

## 2.1. In Range
def in_range(num, lower, upper):
    if (num >= lower and num <= upper):
        return True
    return False
print('2.1')
print(in_range(10,10,10))
print(in_range(5,10,20))

## 2.2. Same Name
def same_name(your_name, my_name):
    if (your_name == my_name):
        return True
    return False
print('2.2')
print(same_name('Geff', 'Jeff'))
print(same_name('Jeff', 'Jeff'))

## 2.3. Always False
def always_false(num):
    if (num < 0 and num > 0):
        return True
    return False
print('2.3')
print(always_false(-1))
print(always_false(0))
print(always_false(1))

## 2.4. Movie Review
def movie_review(rating):
    if rating <= 5:
        return 'Avoid at all costs!'
    if (rating > 5 and rating < 9):
        return 'This one is fun.'
    else:
        return 'Outstanding!'

print('2.4')
print(movie_review(3))
print(movie_review(5))
print(movie_review(8))
print(movie_review(9))
print(movie_review(10))

## 2.5. Movie Review
def max_num(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num1 and num2 > num3):
        return num2
    elif (num3 > num1 and num3 > num2):
        return num3
    else:
        return "It's a tie!"
print(2.5)
print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))

# 3 Lists

## 3.1 Append Size
def append_size(lst):
    lst.append(len(lst))
    return lst
print(3.1)
print(append_size([23, 42, 108]))

## 3.2 Append Sum
###Manual Solution
def append_sum(lst):
    lst.append(lst[-2] + lst[-1])
    lst.append(lst[-2] + lst[-1])
    lst.append(lst[-2] + lst[-1])
    return lst
print(3.2)
print('Manual')
print(append_sum([23, 42, 108]))

###Looped Solution
def append_sum(lst):
    i = 0
    while i < 3:
        lst.append(lst[-2] + lst[-1])
        i += 1
    return lst
print('Looped')
print(append_sum([23, 42, 108]))

## 3.3 Larger List
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return len(lst2)

print(3.3)
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

## 3.4 More Than N
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False
    
print(3.4)
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

## 3.5 Combine Sort
def combine_sort(lst1, lst2):
    combined = lst1 + lst2
    c_s = sorted(combined)
    return c_s

print(3.5)
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

# 4 Advanced Lists

## 4.1 Every Three Numbers
def every_three_nums(start):
    return list(range(start, 101, 3))

print(4.1)
print(every_three_nums(91))

## 4.2 Remove Middle
def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]

print(4.2)
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

## 4.3 More Frequent Item
def more_frequent_item(lst, item1, item2):
    if lst.count([item1]) >= lst.count([item2]):
        return item1
    else:
        return item2

print(4.3)
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

## 4.4 Double Index
def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        new_lst = lst[0:index]
    new_lst.append(lst[index]*2)
    new_lst = new_lst + lst[index+1:]
    return new_lst

print(4.4)
print(double_index([3, 8, -10, 12], 2))

## 4.5 Middle Item
def middle_element(lst):
    if len(lst) % 2 == 0:
        sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
        return sum / 2
    else:
        return lst[int(len(lst)/2)]

print(4.5)
print(middle_element([5, 2, -10, -4, 4, 5]))

# 5 Loops

## 5.1 Divisible By Ten
def divisible_by_ten(nums):
    counter = 0
    for number in nums:
        if (number % 10 == 0):
            counter += 1
    return counter

print(5.1)
print(divisible_by_ten([20, 25, 30, 35, 40]))

## 5.2 Greetings
def add_greetings(names):
    new_lst = []
    for name in names:
        new_lst.append('Hello, ' + name)
    return new_lst

print(5.2)
print(add_greetings(["Owen", "Max", "Sophie"]))

## 5.3 Delete Starting Evens
def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

print(5.3)
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

## 5.4 Odd Indices
def odd_indices(lst):
    new_lst = []
    for index in range(1, len(lst), 2):
        new_lst.append(lst[index])
    return new_lst

print(5.4)
print(odd_indices([4, 3, 7, 10, 11, -2]))

## 5.5 Exponents
def exponents(bases, powers):
    new_lst = []
    for base in bases:
        for power in powers:
            new_lst.append(base ** power)
    return new_lst

print(5.5)
print(exponents([2, 3, 4], [1, 2, 3]))

# 6 Advanced Loops

## 6.1 Larger Sum
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for num1 in lst1:
        sum1 += num1
    for num2 in lst2:
        sum2 += num2
    if sum1 >= sum2:
        return lst1
    else:
        return lst2

print(6.1)
print(larger_sum([1, 9, 5], [2, 3, 7]))

## 6.2 Over Nine Thousand
def over_nine_thousand(lst):
    new_lst = 0
    for num in lst:
        new_lst += num
        if (new_lst > 9000):
            break
    return new_lst

print(6.2)
print(over_nine_thousand([8000, 900, 120, 5000]))

## 6.3 Max Num
def max_num(nums):
    maximum = nums[0]
    for number in nums:
        if number > maximum:
            maximum = number
    return maximum

print(6.3)
print(max_num([50, -10, 0, 75, 20]))

## 6.4 Same Values
def same_values(lst1, lst2):
    new_lst = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_lst.append([index])
    return new_lst

print(6.4)
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

## 6.5 Reversed List
def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True

print(6.5)
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# 7 Functions

## 7.1 Tenth Power
def tenth_power(num):
    return num ** 10

print(7.1)
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

## 7.2 Square Root
def square_root(num):
    return num ** (1/2) # or 0.5

print(7.2)
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

## 7.3 Win Percentage
def win_percentage(wins, losses):
    return (wins / (wins + losses))*100

print(7.3)
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

## 7.4 Average 
def average(num1, num2):
    return (num1 + num2)/2

print(7.4)
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

## 7.5 Remainder
def remainder(num1, num2):
    num1d = num1 * 2
    num2h = num2 / 2
    return num1d % num2h
    # or 'return (num1 * 2)/(num2/2)'

print(7.5)
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# 8 Advanced Functions

## 8.1 First Three Multiples
def first_three_multiples(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3

print(8.1)
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

## 8.2 Tip
def tip(total, percentage):
    return (total * percentage) / 100

print(8.2)
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

## 8.3 Bond, James Bond
def introduction(first_name, last_name):
    return last_name + ', ' + first_name + ' ' + last_name

print(8.3)
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
print(introduction("Big", "Tits"))

## 8.4 Dog Years
def dog_years(name, age):
    return name + ', you are ' + str(age * 7) + ' years old in dog years'
    
print(8.4)    
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

## 8.5 All Operations
def lots_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second
    fourth = third % a
    print(first)
    print(second)
    print(third)
    return(fourth)

print(8.5)
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0