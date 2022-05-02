# Control Flow

## 1. Large Power
def large_power(base, exponent):
    if base**exponent > 5000:
        return True
    else:
        return False

print(large_power(2, 2))
print(large_power(2, 2000))

## 2. Over Budget
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    spent = food_bill + electricity_bill + internet_bill + rent
    if spent > budget:
        return True
    else:
        return False
print(over_budget(100, 20, 30, 10, 40))
print(over_budget(80, 20, 30, 10, 40))

## 3. Twice As Large
def twice_as_large(num1, num2):
    num2_twice = num2*2
    if num2_twice == num1:
        return True
    else:
        return False

print(twice_as_large(10, 5))
print(twice_as_large(11, 5))
print(twice_as_large(9, 5))

## 4. Divisible By Ten
def divisible_by_ten(num):
    if (num % 10 == 0):
        return True
    else:
        return False

print(divisible_by_ten(100))
print(divisible_by_ten(101))

## 5. Not Sum To Ten
def not_sum_to_ten(num1, num2):
    if num1 + num2 != 10:
        return True
    else:
        return False

print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(9, -1))