from . import Constants
class MathOps:
    @staticmethod
    def sum(num1: int | float, num2: int | float) -> int | float:
        if isinstance(num1,(int,float)) and isinstance(num2, (int,float)):
            return num1 + num2
        else:
            raise TypeError("You can only get result of integers or floats")
    @staticmethod
    def sub(num1: int | float, num2: int | float) -> int | float:
        if isinstance(num1,(int,float)) and isinstance(num2, (int,float)):
            return num1 - num2
        else:
            raise TypeError("You can only get result of integers or floats")
    @staticmethod
    def mult(num1: int | float, num2: int | float) -> int | float:
        if isinstance(num1,(int,float)) and isinstance(num2, (int,float)):
            return num1 * num2
        else:
            raise TypeError("You can only get result of integers or floats")
    @staticmethod
    def div(num1: int | float, num2: int | float) -> int | float:
        if isinstance(num1,(int,float)) and isinstance(num2, (int,float)):
            if num2 != 0:
                return num1 / num2
            else:
                raise ZeroDivisionError("You cannot divide any number By zero")
        else:
            raise TypeError("You can only get result of integers or floats")
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
            if num in (0,1):
                return 1
            return cls.fact(num-1) * num
        else:
            raise ValueError("You can only get factorial of integers")
    @staticmethod
    def ln(num: int | float) -> float:
        factor = 0
        while 0 < num > 2:
            num = MathOps.div(num, Constants.e)
            factor += 1
        terms = 1
        base_term = MathOps.div(MathOps.pow(num - 1, terms),terms)
        for _ in range(100):
            terms += 1
            if terms % 2 == 0:
                base_term -= MathOps.div(MathOps.pow(num - 1, terms), terms)
            else:
                base_term += MathOps.div(MathOps.pow(num - 1, terms),terms)
        return base_term + factor
    @staticmethod
    def log(num: int | float, base: int | float) -> float:
        if base <= 0 or base == 1:
            raise ValueError("You can't get the log of a number in base 1 or lower")
        if num <= 0:
            raise ValueError("You can't get a non positive number logarithm")
        return MathOps.div(MathOps.ln(base),MathOps.ln(num))