from illex.decorators.function import function
from illex.decorators.math import math_function


@function("calc")
@function("math") # TODO remover todos os usos de "math"! Incentivar o uso de "calc"
@math_function
def handle_calc(result): return int(result)
