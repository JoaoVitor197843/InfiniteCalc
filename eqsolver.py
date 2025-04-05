from . import MathOps, Constants
class EqSolver:
    @staticmethod
    def delta(a: int | float, b: int | float, c: int | float) -> float | int:
        return MathOps.pow(b) - (4 * a * c)
    @classmethod
    def bhaskara(cls, a: int | float = 1, b: int | float = 0,c: int | float = 0, result: int | float = 0) -> tuple:
        if isinstance(a, (int, float)) and isinstance(b, (int,float)) and isinstance(c, (int,float)) and isinstance(result, (int,float)):
            if a <= 0:
                raise ValueError("A can't be lower or equal a 0")
            if c == 0:
                x2 = cls.related(a, b, result)
                return (0, x2)
            if result != 0:
                c -= result
            x2, x1 = ((-b - MathOps.root(cls.delta(a,b,c))) / (2 * a)), ((-b + MathOps.root(cls.delta(a,b,c))) / (2 * a))
            return (x1, x2)
        else:
            raise TypeError("You can only get result of integers or floats")
    @staticmethod
    def related(a: int | float, b: int | float, result: int | float = 0 ) -> float:
        if isinstance(a, (int, float)) and isinstance(b, (int,float)) and isinstance(result, (int,float)):
            if a == 0:
                return b
            result -= b
            return result / a
        else:
            raise TypeError("You can only get result of integers or floats")