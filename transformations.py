from constants import Constants
class Transformations:
    @staticmethod
    def degree_to_radians(degree: int | float) -> float:
        return degree * ( Constants.pi / 180 )
    @staticmethod
    def radians_to_degree(radians: int | float) -> float:
        return radians * ( 180 / Constants.pi )