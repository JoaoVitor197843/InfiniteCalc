from constants import Constants
from transformations import Transformations
class Operations:
    @staticmethod
    def sum(*nums: int | float) -> int | float:
        if len(nums) < 2:
            raise IndexError("You need to pass 2 numbers or more")
        sum = nums[0]
        for num in nums[1:]:
            if isinstance(num, (int, float)):
               sum += num
            else:
                raise TypeError("You can only get result of integers or floats")
        return sum
    @staticmethod
    def sub(*nums: int | float) -> int | float:
        if len(nums) < 2:
            raise IndexError("You need to pass 2 numbers or more")
        sub = nums[0]
        for num in nums[1:]:
            if isinstance(num, (int, float)):
               sub -= num
            else:
                raise TypeError("You can only get result of integers or floats")
        return sub
    @staticmethod
    def mult(*nums: int | float) -> int | float:
        if len(nums) < 2:
            raise IndexError("You need to pass 2 numbers or more")
        mul = nums[0]
        for num in nums[1:]:
            if isinstance(num, (int, float)):
               mul *= num
            else:
                raise TypeError("You can only get result of integers or floats")
        return mul
    @staticmethod
    def div(*nums: int | float) -> int | float:
        if len(nums) < 2:
            raise IndexError("You need to pass 2 numbers or more")
        div = nums[0]
        for num in nums[1:]:
            if isinstance(num, (int, float)):
               div /= num
            else:
                raise TypeError("You can only get result of integers or floats")
        return div
    @staticmethod
    def pow(num: int | float, power: int | float= 2) -> int | float:
        return num ** power
    @staticmethod
    def root(num: int | float, power: int | float = 2) -> float:
        if isinstance(num, (int, float)) and isinstance(power, (int,float)):
            if num < 0:
                raise ValueError("You can't get a negative number root")
            if power < 1:
                raise ValueError("Your power need to be greater or equal a 1")
            tolerance = 10e-10
            estimative = num / 2
            for _ in range(101):
                next_estimative = ((power-1) * estimative + num / (estimative**(power-1))) / power
                if abs(next_estimative - estimative) < tolerance:
                    return next_estimative
                estimative = next_estimative
            return estimative
        else:
            raise TypeError("You can only get root of integers or floats")
    @classmethod
    def fact(cls,num: int) -> int:
        if isinstance(num, int):
            if num < 0:
                raise ValueError("You can't get a factorial of negative numbers")
            elif num == 0:
                return 1
            else:
                result = 1
                for factorial in range(1,num+1):
                    result *= factorial
                return result
        else:
            raise ValueError("You can only get factorial of integers")
    @staticmethod
    def natural_log(num: int | float) -> float:
        factor = 0
        while 0 < num > 2:
            num = Operations.div(num, Constants.e)
            factor += 1
        base_term = Operations().div(Operations.pow(num - 1, 1),1)
        for terms in range(1,100):
            terms += 1
            if terms % 2 == 0:
                base_term -= Operations.div(Operations.pow(num - 1, terms), terms)
            else:
                base_term += Operations.div(Operations.pow(num - 1, terms),terms)
        return base_term + factor
    @staticmethod
    def log(num: int | float, base: int | float) -> float:
        if base <= 0 or base == 1:
            raise ValueError("You can't get the log of a number in base 1 or lower")
        if num <= 0:
            raise ValueError("You can't get a non positive number logarithm")
        return Operations.div(Operations.natural_log(base),Operations.natural_log(num))
    @classmethod
    def sin(cls, angle: int | float) -> float:
        radians = Transformations.degree_to_radians(angle)
        terms = 3
        base_term = radians - cls.pow(radians,terms) / cls.fact(terms)
        for times in range(20):
            terms += 2
            if times % 2 == 0:
                base_term += cls.pow(radians,terms) / cls.fact(terms)
            else:
                base_term -= cls.pow(radians,terms) / cls.fact(terms)
        return base_term
    @classmethod
    def cos(cls, angle: int | float) -> float:
        radians = Transformations.degree_to_radians(angle)
        terms = 2
        base_term = 1 - cls.pow(radians,terms) / cls.fact(terms)
        for times in range(20):
            terms += 2
            if times % 2 == 0:
                base_term += cls.pow(radians,terms) / cls.fact(terms)
            else:
                base_term -= cls.pow(radians,terms) / cls.fact(terms)
        return base_term
    @classmethod
    def tan(cls, angle: int | float) -> float:
        return cls.sin(angle) / cls.cos(angle)